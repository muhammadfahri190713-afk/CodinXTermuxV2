<div align="center">

# CodinXTermuxV2

### AI coding agent modern untuk Linux, container, dan Termux

Bangun, baca, edit, uji, dan debug proyek langsung dari terminal dengan UI berwarna, tool calling, web search, multi-provider, akun lokal, serta penyimpanan secret terenkripsi.

[![Version](https://img.shields.io/badge/version-1.4.0-7c3aed?style=for-the-badge)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Termux](https://img.shields.io/badge/Termux-supported-00a884?style=for-the-badge)](docs/TERMUX.md)
[![License](https://img.shields.io/badge/license-MIT-22c55e?style=for-the-badge)](LICENSE)

</div>

---

## Apa itu CodinXTermuxV2?

CodinXTermuxV2 adalah coding agent berbasis Python yang berjalan lokal di terminal. CodinX dapat membaca struktur proyek, mengedit file, menjalankan perintah, memakai tool web, mengelola sesi, dan meneruskan pekerjaan ke model yang kamu pilih melalui endpoint OpenAI-compatible.

> **There is Max, Pro and Free. Choose your method**
>
> Pada startup, CodinX menyediakan alur **Sign Up** atau **Log in**. Akun lokal pertama otomatis menjadi admin perangkat.

## Fitur utama

| Area | Kemampuan |
|---|---|
| Coding agent | `read`, `write`, `edit`, `multiedit`, `grep`, `glob`, `bash`, `todo`, `task`, `skill`, `memory`, `camera`, dan MCP |
| Web tools | `websearch` dengan DuckDuckGo Lite + fallback HTML dan `webfetch` dengan method, header, body, serta HTML-to-text |
| Provider | Banyak endpoint OpenAI-compatible melalui `/connect`; model live dapat diambil dari endpoint provider |
| Akun lokal | Sign Up, Log in, auto-login terenkripsi, audit login, dan admin panel lokal |
| UI terminal | Banner, tema, border, spinner, prompt, gutter, Markdown renderer, tabel, syntax highlighting |
| Workflow | Mode `/plan`, `/build`, `/undo`, `/redo`, `/compact`, `/doctor`, sesi persisten, dan sub-agent |
| Platform | Linux, container, dan Termux tanpa root |

## Instalasi cepat

### Linux / container

```bash
git clone https://github.com/muhammadfahri190713-afk/CodinXTermuxV2.git
cd CodinXTermuxV2
python3 bin/codinx
```

### Termux

```bash
pkg update -y
pkg install -y python git

git clone https://github.com/muhammadfahri190713-afk/CodinXTermuxV2.git
cd CodinXTermuxV2
python3 bin/codinx
```

Instalasi permanen opsional:

```bash
bash install.sh
```

## Konfigurasi API melalui `.env`

**Jangan membuat file `.env` lalu melakukan commit atau upload ke repository.** File `.env` hanya untuk mesin yang menjalankan CodinX. Di GitHub, gunakan **Settings → Secrets and variables → Actions** bila key dibutuhkan oleh workflow CI/CD.

Buat file lokal:

```bash
cp .env.example .env
chmod 600 .env
```

Format minimal:

```dotenv
CODINX_BASE_URL=https://inttelix.vercel.app/api/v1
CODINX_API_KEY=ISI_API_KEY_DI_SINI
CODINX_PROVIDER=inttelix
CODINX_MODEL=deepseek-v4-flash
```

Untuk provider lain, ubah endpoint dan key sesuai provider tersebut:

```dotenv
CODINX_BASE_URL=https://openrouter.ai/api/v1
CODINX_API_KEY=ISI_OPENROUTER_KEY_DI_SINI
CODINX_PROVIDER=openrouter
CODINX_MODEL=anthropic/claude-3.7-sonnet
```

Variabel tambahan yang tersedia:

```dotenv
CODINX_TRIAL=1
CODINX_TIER=free
CODINX_TOOL_MODE=auto
CODINX_HISTORY_MODE=auto
CODINX_AUTO_PROBE=1
CODINX_HOME=~/.codinx
```

Selain `.env`, kamu dapat menjalankan wizard koneksi dari dalam aplikasi:

```text
/connect
```

Wizard akan meminta nama provider, endpoint, dan API key. Provider disimpan terenkripsi di `~/.codinx/providers.enc`.

## Login dan admin panel

Saat pertama kali menjalankan mode interaktif, pilih:

```text
1. Sign Up
2. Log in
```

Akun pertama di perangkat otomatis memiliki role admin. Setelah login, panel lokal dapat dibuka dengan:

```text
!cmd admin_panel
```

Panel hanya menampilkan IP lokal dan API key yang sudah disamarkan. Password disimpan sebagai hash PBKDF2 dan sesi login disimpan terenkripsi. Data akun berada di `~/.codinx/accounts.db` dan akan tetap ada sampai folder data CodinX dihapus atau aplikasi di-uninstall.

## Perintah penting

```text
/help                         daftar seluruh perintah
/connect                      tambah atau ubah provider
/providers                    lihat provider tersimpan
/models                       lihat dan pilih model
/doctor                       uji kompatibilitas endpoint, history, dan tools
/plan                         mode read-only
/build                        mode edit aktif
/design opencode              preset UI
/thinking                     tampilkan/sembunyikan indikator thinking
/permissions                  atur izin tool
/sessions                     lanjutkan sesi sebelumnya
```

Contoh non-interaktif:

```bash
python3 bin/codinx run "analisis struktur proyek ini" --plan
python3 bin/codinx run "buat test untuk fungsi login" --auto
python3 bin/codinx run "/skill security-audit proyek ini"
```

## Keamanan

- `.env`, `api.py`, key terenkripsi, akun lokal, sesi, dan log lokal sudah di-ignore oleh Git.
- API key tidak boleh ditulis di source code, README, issue, commit, atau chat publik.
- Jalankan secret scan sebelum push:

```bash
python3 scripts/secret_scan.py .
```

- Jika key pernah terlanjur tersebar, segera revoke dan buat key baru.
- Pembatasan paket FREE/PRO/MAX di sisi klien bukan pengganti enforcement di proxy.

Baca [SECURITY.md](SECURITY.md) untuk kebijakan keamanan dan [docs/GITHUB.md](docs/GITHUB.md) untuk panduan repository.

## Dokumentasi

| Dokumentasi | Link |
|---|---|
| Arsitektur | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Konfigurasi | [docs/CONFIG.md](docs/CONFIG.md) |
| Perintah | [docs/COMMANDS.md](docs/COMMANDS.md) |
| Termux | [docs/TERMUX.md](docs/TERMUX.md) |
| Tool permissions | [docs/PERMISSIONS.md](docs/PERMISSIONS.md) |
| Desain terminal | [docs/DESIGN.md](docs/DESIGN.md) |
| Proxy compatibility | [docs/PROXY_COMPAT.md](docs/PROXY_COMPAT.md) |
| Troubleshooting | [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) |
| Upgrade notes | [docs/UPGRADE_1_4.md](docs/UPGRADE_1_4.md) |

## Pengembangan lokal

```bash
make test
make scan
make docs
make zip
```

## Lisensi

CodinXTermuxV2 dirilis di bawah [MIT License](LICENSE). Dependensi vendor dan lisensinya dijelaskan di [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
