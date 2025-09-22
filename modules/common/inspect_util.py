# modules/common/inspect_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import inspect
from types import FunctionType
from typing import Any


__all__ = [
    "get_function_name",
    "get_caller_name",
    "is_lambda",
]


def get_function_name(fn: Any) -> str:
    """
    Returns the function's name (or <lambda>).
    """
    if not callable(fn):
        return "<not-callable>"
    try:
        return fn.__name__
    except AttributeError:
        return type(fn).__name__


def get_caller_name(level: int = 2) -> str:
    """
    Returns the name of the calling function at the given stack level.
    Default level=2 gives the direct caller.
    """
    try:
        frame = inspect.stack()[level]
        return frame.function
    except Exception:
        return "<unknown>"


def is_lambda(fn: Any) -> bool:
    """
    Returns True if the function is a lambda.
    """
    return isinstance(fn, FunctionType) and fn.__name__ == "<lambda>"
