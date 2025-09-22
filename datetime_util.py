import datetime as __py_dt

__DT__ = __py_dt.datetime
__TZ__ = __py_dt.timezone
from datetime import datetime, timedelta, timezone

DT_FMT = "%Y-%m-%d %H:%M:%S"


def utcnow():
    return datetime.now(timezone.utc)


def epoch():
    return __DT__(1970, 1, 1, tzinfo=__TZ__.utc)


def ensure_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def to_timestamp(dt: datetime) -> int:
    return int((ensure_utc(dt) - epoch()).total_seconds())


def from_timestamp(ts: int) -> datetime:
    return epoch() + timedelta(seconds=int(ts))


def format(dt: datetime) -> str:
    return ensure_utc(dt).strftime(DT_FMT)


def parse(s: str) -> datetime:
    # naive 로 파싱 후 UTC 가정
    return datetime.strptime(s, DT_FMT).replace(tzinfo=timezone.utc)
