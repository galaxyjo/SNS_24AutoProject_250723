# ✅ tests/test_validate.py (디버깅 완료 버전 – 전체 복붙)

import pytest
from modules.common import validate


def test_is_email():
    assert validate.is_email("user@example.com")
    assert validate.is_email("user.name+tag@example.co.uk")
    assert not validate.is_email("user@localhost")  # 도메인 점 없음 → False
    assert not validate.is_email("plainaddress")
    assert not validate.is_email(None)


def test_is_url():
    assert validate.is_url("https://example.com")
    assert validate.is_url("http://example.com")
    assert validate.is_url("ftp://example.com")
    assert not validate.is_url("notaurl")
    assert not validate.is_url(None)


def test_is_numeric():
    assert validate.is_numeric("12345")
    assert not validate.is_numeric("12.34")  # 소수점 포함 → False
    assert not validate.is_numeric("abc123")
    assert not validate.is_numeric("")
    assert not validate.is_numeric(None)


def test_is_alphanumeric():
    assert validate.is_alphanumeric("abc123")
    assert not validate.is_alphanumeric("abc-123")
    assert not validate.is_alphanumeric("123@!")
    assert not validate.is_alphanumeric(None)


def test_is_blank():
    assert validate.is_blank(None)
    assert validate.is_blank("")
    assert validate.is_blank("   ")
    assert not validate.is_blank("abc")
