import pytest
from modules.common import utils
import datetime

def test_formatdate():
    result = utils.formatdate(0, localtime=False, usegmt=True)
    assert "GMT" in result

def test_parseaddr():
    name, email = utils.parseaddr('홍길동 <hong@example.com>')
    assert name == '홍길동'
    assert email == 'hong@example.com'

def test_formataddr_ascii():
    addr = utils.formataddr(("John", "john@example.com"))
    assert addr == 'John <john@example.com>'

def test_formataddr_utf8():
    addr = utils.formataddr(("홍길동", "hong@example.com"))
    assert "=?utf-8?" in addr

def test_make_msgid():
    msgid = utils.make_msgid()
    assert msgid.startswith("<") and msgid.endswith(">")

def test_parsedate_to_datetime():
    date_str = "Mon, 21 Sep 2020 10:00:00 +0000"
    dt = utils.parsedate_to_datetime(date_str)
    assert isinstance(dt, datetime.datetime)
