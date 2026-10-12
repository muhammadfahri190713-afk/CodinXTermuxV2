"""Provider OpenAI-compatible tersimpan terenkripsi di perangkat."""
import json
import os
from . import config, vault
FILE = os.path.join(config.HOME, "providers.enc")

def _load():
    try:
        with open(FILE, "rb") as f:
            return json.loads(vault.decrypt(f.read()))
    except (OSError, ValueError, json.JSONDecodeError):
        return {}

def _save(data):
    config.ensure_dirs()
    tmp = FILE + ".tmp"
    with open(tmp, "wb") as f: f.write(vault.encrypt(json.dumps(data, ensure_ascii=False)))
    os.chmod(tmp, 0o600); os.replace(tmp, FILE)

def list_all():
    return _load()

def upsert(name, base_url, key, model=""):
    name = name.strip().lower()
    if not name or not base_url or not key: raise ValueError("nama, endpoint, dan API key wajib diisi")
    data = _load(); old = data.get(name, {})
    data[name] = {"base_url": config.normalize_url(base_url), "key": key, "model": model or old.get("model", "")}
    _save(data); return data[name]

def remove(name):
    data = _load(); data.pop(name, None); _save(data)

def masked(item):
    return (item[:4] + "…" + item[-4:]) if len(item) > 10 else "••••"
