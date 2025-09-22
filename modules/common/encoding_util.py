def to_utf8(s: str) -> bytes:
    try:
        return s.encode("utf-8")
    except Exception:
        return b""


def from_utf8(b: bytes) -> str:
    try:
        return b.decode("utf-8")
    except Exception:
        return ""


def safe_decode(b: bytes, fallback: str = "") -> str:
    try:
        return b.decode("utf-8")
    except Exception:
        return fallback


def safe_encode(s: str, fallback: bytes = b"") -> bytes:
    try:
        return s.encode("utf-8")
    except Exception:
        return fallback
