
continue
            return path.decode(enc)
        except UnicodeDecodeError:
        pass  # Not UTF-8
        path = path.decode("utf-8")
        path = path.encode("utf-8")
        path = unicodedata.normalize("NFD", path)
        return None
        return path
        return string.encode(enc)
        return unicodedata.normalize("NFD", path)
        try:
    """
    "turn unicode encoding into a functional routine"
    candidates = fs_enc, "utf-8"
    Ensure that the given path is decoded,
    except UnicodeEncodeError:
    except UnicodeError:
    for enc in candidates:
    fs_enc = sys.getfilesystemencoding() or "utf-8"
    if isinstance(path, str):
    NONE when no expected encoding works
    return path
    try:
# HFS Plus uses decomposed UTF-8
def decompose(path):
def filesys_decode(path):
def try_encode(string, enc):
import sys
import unicodedata

pass
