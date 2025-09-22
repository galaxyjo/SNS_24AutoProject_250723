# tests/test_json_util.py

import pytest
from modules.common import json_util as ju


def test_to_json_valid():
    data = {"name": "홍길동", "age": 30}
    json_str = ju.to_json(data)
    assert isinstance(json_str, str)
    assert '"name":' in json_str


def test_to_json_invalid():
    class NotSerializable:
        pass

    assert ju.to_json(NotSerializable()) == ""


def test_from_json_valid():
    s = '{"a": 1, "b": 2}'
    obj = ju.from_json(s)
    assert isinstance(obj, dict)
    assert obj["a"] == 1


def test_from_json_invalid():
    assert ju.from_json("not-json") is None
    assert ju.from_json(None) is None


def test_is_valid_json():
    assert ju.is_valid_json('{"a": 1}')
    assert not ju.is_valid_json("{a:1}")  # 잘못된 JSON
    assert not ju.is_valid_json("")  # 빈 문자열
    assert not ju.is_valid_json(None)  # None 입력
