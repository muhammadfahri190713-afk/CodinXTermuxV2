# System prompt publik

CodinXTermuxV2 memuat instruksi agent dari [`system_prompt.txt`](../system_prompt.txt). File tersebut sengaja public dan dapat diedit untuk menyesuaikan gaya kerja agent dengan kebutuhan proyek.

Prompt ini dirancang dari pola umum agent coding publik: agent memahami repository, menyusun rencana, memakai tool, menjalankan test, membaca error, lalu mengiterasi perbaikan. Untuk browsing, prompt memisahkan pencarian dari pembacaan sumber asli, mendorong verifikasi tanggal/versi, dan meminta sitasi.

Prompt juga memisahkan **data web** dari **instruksi agent**. Halaman eksternal dapat berisi prompt injection, sehingga teks yang meminta model mengabaikan aturan, membocorkan secret, atau menjalankan perintah berbahaya harus diperlakukan sebagai konten tidak tepercaya.

## Referensi

- [1] [GitHub Copilot on GitHub.com — coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent): workflow research, plan, edit, test, dan review.
- [2] [GitHub Blog — Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/): loop iteratif, tool eksternal, pemeriksaan error, dan custom instructions.
- [3] [OpenAI — Best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api): instruksi spesifik, pemisahan konteks, format output, dan tindakan alternatif yang jelas.
- [4] [EliFuzz/awesome-system-prompts](https://github.com/EliFuzz/awesome-system-prompts): indeks publik prompt dan dokumentasi tool dari berbagai coding agent; digunakan sebagai referensi pola, bukan disalin mentah.
- [5] [tallesborges/agentic-system-prompts](https://github.com/tallesborges/agentic-system-prompts): koleksi prompt, tool definition, atribusi, dan pola keamanan agent coding.

Sumber diperiksa pada 12 Oktober 2026. Prompt CodinX adalah tulisan baru untuk project ini, bukan salinan system prompt proprietary.
