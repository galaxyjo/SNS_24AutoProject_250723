# tests/test_sort_helper.py

import pytest
from modules.common.sort_helper import sort_by, sort_dict_by_key, sort_dict_by_value


def test_sort_by_basic():
    data = ["banana", "apple", "cherry"]
    result = sort_by(data, key_func=len)
    assert result == ["apple", "banana", "cherry"]


def test_sort_by_reverse():
    data = ["a", "bbb", "cc"]
    result = sort_by(data, key_func=len, reverse=True)
    assert result == ["bbb", "cc", "a"]


def test_sort_dict_by_key():
    data = {"b": 2, "a": 1, "c": 3}
    result = sort_dict_by_key(data)
    assert list(result.keys()) == ["a", "b", "c"]


def test_sort_dict_by_value():
    data = {"apple": 3, "banana": 1, "cherry": 2}
    result = sort_dict_by_value(data)
    assert list(result.keys()) == ["banana", "cherry", "apple"]


def test_sort_dict_by_value_reverse():
    data = {"x": 10, "y": 30, "z": 20}
    result = sort_dict_by_value(data, reverse=True)
    assert list(result.keys()) == ["y", "z", "x"]
