# modules/common/date_util.py

"""Date utility functions for parsing, formatting, and simple calculations."""

from __future__ import annotations
from datetime import datetime, timedelta, date
from typing import Optional


def parse_date(s: Optional[str], fmt: str = "%Y-%m-%d") -> Optional[date]:
    """Parse a date string to a date object. Return None if invalid."""
    if not s:
        return None
    try:
        return datetime.strptime(s, fmt).date()
    except Exception:
        return None


def format_date(d: Optional[date], fmt: str = "%Y-%m-%d") -> str:
    """Format a date object to string. Return empty string if None."""
    if not d:
        return ""
    return d.strftime(fmt)


def today(fmt: Optional[str] = None) -> str | date:
    """Return today's date. Formatted if fmt is given."""
    d = date.today()
    return d.strftime(fmt) if fmt else d


def add_days(d: Optional[date], days: int) -> Optional[date]:
    """Add days to a date object."""
    if not d:
        return None
    return d + timedelta(days=days)


def days_between(d1: Optional[date], d2: Optional[date]) -> Optional[int]:
    """Return number of days between two dates."""
    if not d1 or not d2:
        return None
    return (d2 - d1).days


__all__ = [
    "parse_date",
    "format_date",
    "today",
    "add_days",
    "days_between",
]
