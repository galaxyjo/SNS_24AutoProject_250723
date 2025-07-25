
                "Cannot process 'custom' argument on a compiled selector list"
                "Cannot process 'flags' argument on a compiled selector list"
                "Cannot process 'namespaces' argument on a compiled selector list"
            )
            raise ValueError(
        ct.CustomSelectors(custom) if custom is not None else custom,
        ct.Namespaces(namespaces) if namespaces is not None else namespaces,
        elif custom is not None:
        elif namespaces is not None:
        flags,
        if flags:
        pattern,
        return pattern
    """Compile CSS pattern."""
    """Escape identifier."""
    """Filter list of nodes."""
    """Iterate the specified tags."""
    """Match closest ancestor."""
    """Match node."""
    """Purge cached patterns."""
    """Select a single tag."""
    """Select the specified tags."""
    "closest",
    "compile",
    "DEBUG",
    "filter",
    "iselect",
    "match",
    "select",
    "select_one",
    "SelectorSyntaxError",
    "SoupSieve",
    )
    **kwargs: Any,
    *,
    cp._purge_cache()
    custom: dict[str, str] | None = None,
    flags: int = 0,
    if isinstance(pattern, SoupSieve):
    iterable: Iterable[bs4.Tag],
    limit: int = 0,
    namespaces: dict[str, str] | None = None,
    pattern: str,
    return compile(select, namespaces, flags, **kwargs).closest(tag)
    return compile(select, namespaces, flags, **kwargs).filter(iterable)
    return compile(select, namespaces, flags, **kwargs).match(tag)
    return compile(select, namespaces, flags, **kwargs).select(tag, limit)
    return compile(select, namespaces, flags, **kwargs).select_one(tag)
    return cp._cached_css_compile(
    return cp.escape(ident)
    select: str,
    tag: bs4.Tag,
    yield from compile(select, namespaces, flags, **kwargs).iselect(tag, limit)
"""
)
) -> bool:
) -> bs4.Tag | None:
) -> cm.SoupSieve:
) -> Iterator[bs4.Tag]:
) -> list[bs4.Tag]:
__all__ = (
A CSS selector filter for BeautifulSoup4.
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
copies of the Software, and to permit persons to whom the Software is
copies or substantial portions of the Software.
Copyright (c) 2018 Isaac Muse
def closest(
def compile(  # noqa: A001
def escape(ident: str) -> str:
def filter(  # noqa: A001
def iselect(
def match(
def purge() -> None:
def select(
def select_one(
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
from . import css_match as cm
from . import css_parser as cp
from . import css_types as ct
from .__meta__ import __version__, __version_info__  # noqa: F401
from .util import DEBUG, SelectorSyntaxError  # noqa: F401
from __future__ import annotations
from typing import Any, Iterator, Iterable
furnished to do so, subject to the following conditions:
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
import bs4
in the Software without restriction, including without limitation the rights
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
MIT License
of this software and associated documentation files (the "Software"), to deal
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
Permission is hereby granted, free of charge, to any person obtaining a copy
SOFTWARE.
Soup Sieve.
SoupSieve = cm.SoupSieve
The above copyright notice and this permission notice shall be included in all
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
