# modules/common/string_util.py
"""String utility helpers for normalization, casing, slugging, and safe operations.

This module contains only pure, deterministic functions with no external I/O.
Designed for unit-test friendliness and high coverage.
"""

from __future__ import annotations

import re
import unicodedata
from html import unescape
from typing import Iterable, Optional, List


def is_blank(s: Optional[str]) -> bool:
    """Return True if s is None or consists only of whitespace characters."""
    return s is None or s.strip() == ""


def normalize_whitespace(s: Optional[str], *, keep_newlines: bool = False) -> str:
    """Normalize whitespace.

    - If keep_newlines=False: collapse all runs of whitespace to a single space.
    - If keep_newlines=True: preserve line breaks while collapsing intra-line spaces.

    None → "".
    """
    if s is None:
        return ""
    if not keep_newlines:
        # Simple, robust: split() collapses all whitespace, including newlines.
        return " ".join(s.split())
    # Preserve newlines: collapse spaces/tabs per line, and compress multiple blank lines.
    text = re.sub(r"[^\S\n]+", " ", s)  # collapse spaces/tabs but keep \n
    text = re.sub(r"\n{2,}", "\n", text)  # compress multiple newlines
    return text.strip()


def safe_lower(s: Optional[str]) -> str:
    """Lowercase string; None → ''."""
    return "" if s is None else s.lower()


def safe_upper(s: Optional[str]) -> str:
    """Uppercase string; None → ''."""
    return "" if s is None else s.upper()


def truncate(s: Optional[str], max_len: int, *, ellipsis: str = "…") -> str:
    """Truncate string to max_len, appending ellipsis if truncated.

    Rules:
    - max_len < 0 → ValueError
    - None → ""
    - If len(s) <= max_len → s unchanged
    - If max_len < len(ellipsis) → ellipsis[:max_len]
    """
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
    """Remove accents/diacritics using NFKD normalization. None → ''."""
    if s is None:
        return ""
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def to_slug(s: Optional[str], *, allow_unicode: bool = False, sep: str = "-") -> str:
    """Create a URL-friendly slug.

    Steps:
    1) None → ""
    2) Lowercase
    3) If not allow_unicode: remove accents, ASCII-only
    4) Replace non-word runs with sep; collapse repeats; trim sep
    """
    if s is None:
        return ""
    text = s.lower()
    if not allow_unicode:
        text = remove_accents(text)
        text = text.encode("ascii", "ignore").decode("ascii")
    # Replace non-word characters with separator. \w is unicode-aware when allow_unicode=True.
    text = re.sub(r"[^\w]+", sep, text, flags=re.UNICODE)
    text = re.sub(rf"{re.escape(sep)}+", sep, text).strip(sep)
    return text


def to_snake_case(s: Optional[str]) -> str:
    """Convert string to snake_case.

    Handles:
    - CamelCase → snake_case
    - spaces/hyphens → underscores
    - collapse multiple underscores
    """
    if not s:
        return ""
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)  # camel to snake boundary
    text = re.sub(r"[\s\-]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_").lower()


def to_camel_case(s: Optional[str], *, upper_first: bool = False) -> str:
    """Convert string to camelCase (default) or PascalCase (upper_first=True)."""
    if not s:
        return ""
    parts = re.split(r"[^0-9A-Za-z]+", s.strip())
    parts = [p for p in parts if p]
    if not parts:
        return ""
    first = parts[0].lower() if not upper_first else parts[0].capitalize()
    rest = [p.capitalize() for p in parts[1:]]
    return "".join([first] + rest)


def strip_html(s: Optional[str]) -> str:
    """Remove HTML tags and unescape entities. None → ''."""
    if s is None:
        return ""
    no_tags = re.sub(r"<[^>]+>", "", s)
    return unescape(no_tags)


def split_words(s: Optional[str]) -> List[str]:
    """Split by whitespace into tokens. None/blank → []"""
    if s is None:
        return []
    tokens = re.split(r"\s+", s.strip())
    return [t for t in tokens if t]


def join_non_empty(parts: Iterable[Optional[str]], *, sep: str = " ") -> str:
    """Join non-empty/ non-blank items with sep. None/blank filtered out."""
    filtered = [p for p in parts if p and str(p).strip()]
    return sep.join(str(p) for p in filtered)


__all__ = [
    "is_blank",
    "normalize_whitespace",
    "safe_lower",
    "safe_upper",
    "truncate",
    "remove_accents",
    "to_slug",
    "to_snake_case",
    "to_camel_case",
    "strip_html",
    "split_words",
    "join_non_empty",
]
