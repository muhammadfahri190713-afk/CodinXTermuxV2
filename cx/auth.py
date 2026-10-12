"""Autentikasi lokal CodinX: SQLite, hash PBKDF2, dan audit tanpa password."""
import hashlib
import hmac
import os
import secrets
import socket
import sqlite3
import time
import json
from . import config, vault

DB = os.path.join(config.HOME, "accounts.db")
SESSION = os.path.join(config.HOME, "login.enc")

def _db():
    config.ensure_dirs()
    con = sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript("""
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL,
      password_hash TEXT NOT NULL, created_at REAL NOT NULL,
      last_login REAL, last_ip TEXT, is_admin INTEGER NOT NULL DEFAULT 0
    );
    CREATE TABLE IF NOT EXISTS audit (
      id INTEGER PRIMARY KEY, username TEXT, action TEXT NOT NULL,
      at REAL NOT NULL, ip TEXT, detail TEXT
    );
    """)
    return con

def _ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except OSError:
        return "unknown"

def _hash(password, salt=None):
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 240_000)
    return salt.hex() + ":" + digest.hex()

def _check(password, encoded):
    try:
        salt, expected = encoded.split(":", 1)
        got = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 240_000).hex()
        return hmac.compare_digest(got, expected)
    except (ValueError, TypeError):
        return False

def count_users():
    with _db() as con:
        return con.execute("SELECT COUNT(*) FROM users").fetchone()[0]

def signup(username, password):
    username = username.strip().lower()
    if not (3 <= len(username) <= 48) or not username.replace("_", "").replace("-", "").isalnum():
        return False, "Username 3–48 karakter, hanya huruf, angka, '-' atau '_'."
    if len(password) < 8:
        return False, "Password minimal 8 karakter."
    con = _db(); now = time.time(); ip = _ip()
    try:
        first = con.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0
        con.execute("INSERT INTO users(username,password_hash,created_at,last_login,last_ip,is_admin) VALUES(?,?,?,?,?,?)",
                    (username, _hash(password), now, now, ip, int(first)))
        con.execute("INSERT INTO audit(username,action,at,ip,detail) VALUES(?,?,?,?,?)", (username, "signup", now, ip, "admin pertama" if first else ""))
        con.commit()
        return True, "Akun dibuat dan sesi login disimpan di perangkat ini."
    except sqlite3.IntegrityError:
        return False, "Username sudah terdaftar."
    finally:
        con.close()

def login(username, password):
    con = _db(); row = con.execute("SELECT username,password_hash,is_admin FROM users WHERE username=?", (username.strip().lower(),)).fetchone()
    if not row or not _check(password, row[1]):
        con.execute("INSERT INTO audit(username,action,at,ip,detail) VALUES(?,?,?,?,?)", (username.strip().lower(), "login_failed", time.time(), _ip(), "")); con.commit(); con.close()
        return False, None, "Username atau password salah."
    now = time.time(); ip = _ip()
    con.execute("UPDATE users SET last_login=?,last_ip=? WHERE username=?", (now, ip, row[0]))
    con.execute("INSERT INTO audit(username,action,at,ip,detail) VALUES(?,?,?,?,?)", (row[0], "login", now, ip, "")); con.commit(); con.close()
    return True, {"username": row[0], "is_admin": bool(row[2])}, "Login berhasil."

def users():
    with _db() as con:
        return con.execute("SELECT username,created_at,last_login,last_ip,is_admin FROM users ORDER BY created_at").fetchall()

def audit(limit=100):
    with _db() as con:
        return con.execute("SELECT username,action,at,ip,detail FROM audit ORDER BY at DESC LIMIT ?", (limit,)).fetchall()


def remember(user):
    config.ensure_dirs()
    with open(SESSION, "wb") as f: f.write(vault.encrypt(json.dumps(user)))
    os.chmod(SESSION, 0o600)

def current():
    try:
        with open(SESSION, "rb") as f: return json.loads(vault.decrypt(f.read()))
    except (OSError, ValueError, json.JSONDecodeError): return None
