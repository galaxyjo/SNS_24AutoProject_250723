# tests/test_sort_util.py

import pytest
from modules.common.sort_util import sort_list, sort_dict_by_key, sort_dict_by_value


def test_sort_list_basic():
    assert sort_list([3, 1, 2]) == [1, 2, 3]


def test_sort_list_reverse():
    assert sort_list([3, 1, 2], reverse=True) == [3, 2, 1]


def test_sort_list_key_lambda():
    assert sort_list(["apple", "banana", "kiwi"], key=lambda x: len(x)) == [
        "kiwi",
        "apple",
        "banana",
    ]


def test_sort_dict_by_key_basic():
    d = {"b": 2, "a": 1, "c": 3}
    assert sort_dict_by_key(d) == {"a": 1, "b": 2, "c": 3}


def test_sort_dict_by_key_reverse():
    d = {"b": 2, "a": 1, "c": 3}
    assert sort_dict_by_key(d, reverse=True) == {"c": 3, "b": 2, "a": 1}


def test_sort_dict_by_value_basic():
    d = {"x": 30, "y": 10, "z": 20}
    assert sort_dict_by_value(d) == {"y": 10, "z": 20, "x": 30}


def test_sort_dict_by_value_reverse():
    d = {"x": 30, "y": 10, "z": 20}
    assert sort_dict_by_value(d, reverse=True) == {"x": 30, "z": 20, "y": 10}


def test_sort_list_invalid_input():
    result = sort_list([3, "a", 2])
    assert isinstance(
        result, list
    )  # Should handle error and return empty or partial list


def test_sort_dict_by_key_invalid_input():
    assert sort_dict_by_key(None) == {}


def test_sort_dict_by_value_invalid_input():
    assert sort_dict_by_value(None) == {}
