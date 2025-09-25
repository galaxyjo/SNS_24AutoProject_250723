import sys
import unicodedata

def decompose(path):
    """
    Decomposes a unicode path string for compatibility with filesystems like HFS+.
    """
    if isinstance(path, str):
        return unicodedata.normalize("NFD", path)
    try:
        fs_enc = sys.getfilesystemencoding() or "utf-8"
        path = path.decode(fs_enc)
        return unicodedata.normalize("NFD", path)
    except (UnicodeError, AttributeError):
        return path

def filesys_decode(path):
    """
    Attempts to decode a byte path using filesystem encoding or utf-8.
    Returns the original path if decoding fails.
    """
    if isinstance(path, str):
        return path

    candidates = [sys.getfilesystemencoding() or "utf-8", "utf-8"]

    for enc in candidates:
        try:
            return path.decode(enc)
        except UnicodeDecodeError:
            continue

    return path  # fallback, return original

def try_encode(string, enc):
    """
    Tries to encode a string using the specified encoding.
    Returns None if encoding fails.
    """
    try:
        return string.encode(enc)
    except UnicodeEncodeError:
        return None
