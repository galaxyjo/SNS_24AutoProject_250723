import re, unicodedata
from html import unescape
from typing import Iterable, Optional, List


def is_blank(s: Optional[str]) -> bool:
    return s is None or s.strip() == ""


def normalize_whitespace(s: Optional[str], *, keep_newlines: bool = False) -> str:
    if s is None:
        return ""
    if not keep_newlines:
        return " ".join(s.split())
    t = re.sub(r"[^\S\n]+", " ", s)
    t = re.sub(r"\n{2,}", "\n", t)
    return t.strip()


def safe_lower(s: Optional[str]) -> str:
    return "" if s is None else s.lower()


def safe_upper(s: Optional[str]) -> str:
    return "" if s is None else s.upper()


def truncate(s: Optional[str], max_len: int, *, ellipsis: str = "…") -> str:
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    if s is None:
        return ""
    if len(s) <= max_len:
        return s
    if max_len <= len(ellipsis):
        return ellipsis[:max_len]
    return s[: max_len - len(ellipsis)] + ellipsis


def remove_accents(s: Optional[str]) -> str:
    if s is None:
        return ""
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def to_slug(s: Optional[str], *, allow_unicode: bool = False, sep: str = "-") -> str:
    if s is None:
        return ""
    text = s.lower()
    if not allow_unicode:
        text = remove_accents(text)
        text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w]+", sep, text, flags=re.UNICODE)
    text = re.sub(rf"{re.escape(sep)}+", sep, text).strip(sep)
    return text


def to_snake_case(s: Optional[str]) -> str:
    if not s:
        return ""
    t = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    t = re.sub(r"[\s\-]+", "_", t)
    t = re.sub(r"_+", "_", t)
    return t.strip("_").lower()


def to_camel_case(s: Optional[str], *, upper_first: bool = False) -> str:
    if not s:
        return ""
    parts = [p for p in re.split(r"[^0-9A-Za-z]+", s.strip()) if p]
    if not parts:
        return ""
    first = parts[0].lower() if not upper_first else parts[0].capitalize()
    rest = [p.capitalize() for p in parts[1:]]
    return "".join([first] + rest)


def strip_html(s: Optional[str]) -> str:
    if s is None:
        return ""
    return unescape(re.sub(r"<[^>]+>", "", s))


def split_words(s: Optional[str]) -> List[str]:
    if s is None:
        return []
    tokens = re.split(r"\s+", s.strip())
    return [t for t in tokens if t]


def join_non_empty(parts: Iterable[Optional[str]], *, sep: str = " ") -> str:
    filtered = [p for p in parts if p and str(p).strip()]
    return sep.join(str(p) for p in filtered)
