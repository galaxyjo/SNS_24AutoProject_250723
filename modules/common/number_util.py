# modules/common/number_util.py

"""Utility functions for numerical operations like clamping, rounding, safe parsing."""

from typing import Optional, Union


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Clamp value between min_value and max_value."""
    return max(min_value, min(value, max_value))


def round_to(value: float, decimals: int = 0) -> float:
    """Round number to a given number of decimal places."""
    return round(value, decimals)


def safe_int(value: Optional[Union[str, float, int]]) -> Optional[int]:
    """Convert to int if possible, else return None."""
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def safe_float(value: Optional[Union[str, float, int]]) -> Optional[float]:
    """Convert to float if possible, else return None."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def is_numeric(value: any) -> bool:
    """Return True if value is int or float-like (parsable)."""
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


__all__ = [
    "clamp",
    "round_to",
    "safe_int",
    "safe_float",
    "is_numeric",
]
