"""Client API pembantu CodinXTermuxV2.

Konfigurasi helper hanya dibaca dari environment/.env/helper_api.py dan tidak
pernah dimasukkan ke config utama atau log.
"""
from . import api, config

def settings():
    return {
        "base_url": config.normalize_url(config.env("CODINX_HELPER_BASE_URL") or config.DEFAULT_HELPER_BASE_URL),
        "model": config.env("CODINX_HELPER_MODEL") or config.DEFAULT_HELPER_MODEL,
        "temperature": None,
        "insecure_tls": False,
        "conv_field": "",
    }

def key():
    return config.env("CODINX_HELPER_API_KEY")

def available():
    return bool(key())

def chat(messages, tools=None, on_text=None, on_reasoning=None, timeout=600):
    """Panggil helper secara eksplisit; tidak pernah fallback atau menimpa provider utama."""
    if not available():
        raise api.ApiError("API pembantu belum dikonfigurasi. Isi helper_api.py atau CODINX_HELPER_API_KEY.")
    return api.chat(settings(), key(), messages, tools=tools, on_text=on_text, on_reasoning=on_reasoning, timeout=timeout)
