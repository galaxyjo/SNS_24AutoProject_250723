# modules/common/logical_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

from typing import Any


__all__ = [
    "coalesce",
    "is_truthy",
    "is_falsy",
]


def coalesce(*args: Any) -> Any:
    """
    Returns the first argument that is not None.
    If all are None, returns None.
    """
    for arg in args:
        if arg is not None:
            return arg
    return None


def is_truthy(val: Any) -> bool:
    """
    Returns True if the value is logically truthy.
    """
    return bool(val)


def is_falsy(val: Any) -> bool:
    """
    Returns True if the value is logically falsy.
    """
    return not bool(val)
