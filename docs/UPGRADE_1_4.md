# CodinX 1.4 — akun, provider, dan web tools

## Perubahan

- Banner startup menampilkan: `There is Max, Pro and Free. Choose your method` lalu pilihan **Sign Up / Log in**.
- Akun lokal tersimpan di `~/.codinx/accounts.db`; password memakai PBKDF2-HMAC-SHA256 dan tidak pernah disimpan plaintext.
- Sesi login disimpan terenkripsi di `~/.codinx/login.enc` dan dipulihkan otomatis pada peluncuran berikutnya.
- Akun pertama menjadi admin lokal. Akses panel melalui `!cmd admin_panel` setelah login.
- Panel menampilkan akun, audit login, provider, dan IP lokal; API key selalu disamarkan.
- `/connect` sekarang meminta nama provider, endpoint, dan API key. Provider disimpan terenkripsi di `~/.codinx/providers.enc`.
- `/providers` menampilkan daftar provider dan key yang sudah dimask. Model live tetap diambil dari endpoint aktif melalui `/models`.
- `websearch` memakai DuckDuckGo Lite sebagai jalur utama dan HTML DuckDuckGo sebagai fallback; parser menerima variasi atribut HTML.
- `webfetch` tetap mendukung method HTTP, header, body, HTML-to-text, batas ukuran respons, dan izin localhost.

## Keamanan

- Jangan menaruh API key di source, commit, log, atau mengirimkannya di chat.
- API key yang pernah ditempelkan di tempat yang bukan brankas harus segera **dicabut/dirotasi** dari provider terkait.
- Gunakan `chmod 600` untuk `.env` atau `api.py`; file tersebut sudah di-ignore oleh Git.
- Admin panel adalah panel perangkat lokal, bukan server web dan tidak membuka port jaringan.

## Pengujian

Validasi yang dijalankan:

- `python3 -m compileall -q cx tests`
- import semua modul inti
- pencarian live DuckDuckGo Lite menghasilkan hasil
- fetch live `https://example.com` menghasilkan HTTP 200
- signup, login benar/salah, penyimpanan terenkripsi provider, dan masking key
