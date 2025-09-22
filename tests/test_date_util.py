# tests/test_date_util.py

import pytest
import datetime
from datetime import date
from modules.common import date_util as du


def test_parse_date_valid():
    assert du.parse_date("2024-01-01") == date(2024, 1, 1)
    assert du.parse_date("1999-12-31", fmt="%Y-%m-%d") == date(1999, 12, 31)


def test_parse_date_invalid():
    assert du.parse_date("2024/01/01") is None
    assert du.parse_date("") is None
    assert du.parse_date(None) is None


def test_format_date_valid():
    d = date(2024, 8, 31)
    assert du.format_date(d) == "2024-08-31"
    assert du.format_date(d, fmt="%d/%m/%Y") == "31/08/2024"


def test_format_date_none():
    assert du.format_date(None) == ""


def test_today_formats(monkeypatch):
    today = datetime.date.today()
    expected_str = today.strftime("%Y/%m/%d")
    assert du.today() == today
    assert du.today(fmt="%Y/%m/%d") == expected_str


def test_add_days():
    d = date(2024, 1, 1)
    assert du.add_days(d, 10) == date(2024, 1, 11)
    assert du.add_days(d, -1) == date(2023, 12, 31)
    assert du.add_days(None, 5) is None


def test_days_between():
    d1 = date(2024, 1, 1)
    d2 = date(2024, 1, 31)
    assert du.days_between(d1, d2) == 30
    assert du.days_between(d2, d1) == -30
    assert du.days_between(None, d2) is None
    assert du.days_between(d1, None) is None
