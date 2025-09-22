# modules/common/error_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import traceback
from typing import Optional


__all__ = [
    "extract_exception_message",
    "format_exception_trace",
]


def extract_exception_message(exc: BaseException, default: Optional[str] = None) -> str:
    """
    Extracts a clean error message from an exception instance.
    Falls back to default message if available.
    """
    if not exc:
        return default or "Unknown error"
    msg = str(exc).strip()
    return msg if msg else (default or exc.__class__.__name__)


def format_exception_trace(exc: BaseException) -> str:
    """
    Returns full traceback string of an exception.
    """
    return "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
