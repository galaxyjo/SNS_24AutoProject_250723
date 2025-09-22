import pytest
from modules.common import encoding_util


def test_to_utf8_success():
    assert encoding_util.to_utf8("hello") == b"hello"


def test_to_utf8_fail():
    class BadStr:
        def encode(self, _):
            raise ValueError("fail")

    assert encoding_util.to_utf8(BadStr()) == b""


def test_from_utf8_success():
    assert encoding_util.from_utf8(b"hello") == "hello"


def test_from_utf8_fail():
    assert encoding_util.from_utf8(b"\xff\xff") == ""


def test_safe_decode_with_fallback():
    assert encoding_util.safe_decode(b"\xff", fallback="fallback") == "fallback"


def test_safe_encode_with_fallback():
    class BadStr:
        def encode(self, _):
            raise ValueError("fail")

    assert encoding_util.safe_encode(BadStr(), fallback=b"default") == b"default"
