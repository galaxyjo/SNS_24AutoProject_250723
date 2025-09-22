# tests/test_time_util.py

from datetime import datetime
import modules.common.time_util as time_util


def test_get_utc_now():
    now = time_util.get_utc_now()
    assert isinstance(now, datetime)
    assert now.tzinfo is not None


def test_format_datetime():
    dt = datetime(2025, 1, 1, 12, 0, 0)
    formatted = time_util.format_datetime(dt)
    assert formatted == "2025-01-01 12:00:00"


def test_parse_datetime_valid():
    dt_str = "2025-01-01 12:00:00"
    parsed = time_util.parse_datetime(dt_str)
    assert parsed.year == 2025
    assert parsed.month == 1
    assert parsed.hour == 12


def test_parse_datetime_invalid():
    assert time_util.parse_datetime("not-a-date") is None
