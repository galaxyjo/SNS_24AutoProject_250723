# modules/common/json_util.py

"""JSON utility functions with safe defaults and fallback handling."""

import json
from typing import Any, Optional


def to_json(
    data: Any, *, ensure_ascii: bool = False, indent: Optional[int] = None
) -> str:
    """Convert Python object to JSON string."""
    try:
        return json.dumps(data, ensure_ascii=ensure_ascii, indent=indent)
    except (TypeError, OverflowError):
        return ""


def from_json(s: str) -> Optional[Any]:
    """Convert JSON string to Python object."""
    try:
        return json.loads(s)
    except (json.JSONDecodeError, TypeError):
        return None


def is_valid_json(s: str) -> bool:
    """Check if string is valid JSON."""
    try:
        json.loads(s)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


__all__ = [
    "to_json",
    "from_json",
    "is_valid_json",
]
