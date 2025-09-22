from datetime import datetime

import pytest

from modules.common import time_helper


def test_get_now_timestamp():
    result = time_helper.get_now_timestamp()
    assert isinstance(result, str)
    assert len(result) > 0


def test_format_datetime():
    dt_str = "2025-08-13 12:34:56"
    result = time_helper.format_datetime(dt_str)
    assert isinstance(result, str)
    assert "2025" in result


def test_parse_datetime():
    dt_str = "2025-08-13 12:34:56"
    result = time_helper.parse_datetime(dt_str)
    assert isinstance(result, datetime)


def test_add_seconds():
    dt_str = "2025-08-13 12:34:56"
    result = time_helper.add_seconds(dt_str, 60)
    assert "12:35" in result


def test_diff_in_seconds():
    dt1 = "2025-08-13 12:34:56"
    dt2 = "2025-08-13 12:35:56"
    result = time_helper.diff_in_seconds(dt1, dt2)
    assert result == 60
