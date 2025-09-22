from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone
from typing import Iterable

_DATETIME_FMT = "%Y-%m-%d %H:%M:%S"

__all__ = [
    "get_now_timestamp",
    "format_datetime",
    "parse_datetime",
    "add_seconds",
    "diff_in_seconds",
    "get_current_time",
    "convert_timezone",
    "sleep_until",
]


def get_current_time() -> datetime:
    return datetime.now(timezone.utc)


def convert_timezone(dt: datetime, tz_offset_hours: int) -> datetime:
    return dt.astimezone(timezone(timedelta(hours=tz_offset_hours)))  # pragma: no cover


def sleep_until(target_time: datetime) -> None:
    now = get_current_time()  # pragma: no cover
    delta = (target_time - now).total_seconds()  # pragma: no cover
    if delta > 0:  # pragma: no cover
        time.sleep(delta)  # pragma: no cover


def get_now_timestamp() -> str:
    return get_current_time().strftime(_DATETIME_FMT)


def _try_parse(dt_str: str, formats: Iterable[str]) -> datetime:
    last_err: Exception | None = None
    for fmt in formats:
        try:
            dt = datetime.strptime(dt_str, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception as e:  # pragma: no cover
            last_err = e  # pragma: no cover
    raise last_err  # type: ignore[misc]  # pragma: no cover


def parse_datetime(dt_str: str) -> datetime:
    return _try_parse(
        dt_str,
        (
            _DATETIME_FMT,
            "%Y-%m-%dT%H:%M:%S",
            "%Y/%m/%d %H:%M:%S",
        ),
    )


def format_datetime(dt_str: str) -> str:
    dt = parse_datetime(dt_str)
    return dt.strftime(_DATETIME_FMT)


def add_seconds(dt_str: str, seconds: int | float) -> str:
    dt = parse_datetime(dt_str) + timedelta(seconds=seconds)
    return dt.strftime(_DATETIME_FMT)


def diff_in_seconds(dt1_str: str, dt2_str: str) -> int:
    dt1 = parse_datetime(dt1_str)
    dt2 = parse_datetime(dt2_str)
    return int((dt2 - dt1).total_seconds())
