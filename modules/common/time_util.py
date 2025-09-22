# modules/common/time_util.py

from datetime import datetime, timezone
from typing import Optional


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    return dt.strftime(fmt)


def parse_datetime(dt_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> Optional[datetime]:
    try:
        return datetime.strptime(dt_str, fmt).replace(tzinfo=timezone.utc)
    except ValueError:
        return None
