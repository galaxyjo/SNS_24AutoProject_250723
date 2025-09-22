# modules/common/type_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

from typing import Any


__all__ = [
    "is_iterable_but_not_str",
    "is_dict_like",
    "is_list_like",
    "is_empty",
]


def is_iterable_but_not_str(obj: Any) -> bool:
    """
    Returns True if object is iterable but not a string.
    """
    if isinstance(obj, str):
        return False
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def is_dict_like(obj: Any) -> bool:
    """
    Returns True if object behaves like a dictionary.
    """
    return isinstance(obj, dict)


def is_list_like(obj: Any) -> bool:
    """
    Returns True if object behaves like a list/tuple/set (but not string).
    """
    return isinstance(obj, (list, tuple, set))


def is_empty(obj: Any) -> bool:
    """
    Returns True if object is empty (len == 0).
    """
    try:
        return len(obj) == 0
    except Exception:
        return False
