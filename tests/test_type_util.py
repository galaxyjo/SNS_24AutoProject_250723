# tests/test_type_util.py
# UTF-8 (no BOM), LF

from __future__ import annotations

import pytest

from modules.common.type_util import (
    is_iterable_but_not_str,
    is_dict_like,
    is_list_like,
    is_empty,
)


@pytest.mark.parametrize(
    "val,expected",
    [
        ([1, 2], True),
        ((1, 2), True),
        (set([1]), True),
        ("abc", False),
        (123, False),
    ],
)
def test_is_iterable_but_not_str(val, expected):
    assert is_iterable_but_not_str(val) == expected


@pytest.mark.parametrize(
    "val,expected",
    [
        ({"a": 1}, True),
        ([], False),
        ("a", False),
        (None, False),
    ],
)
def test_is_dict_like(val, expected):
    assert is_dict_like(val) == expected


@pytest.mark.parametrize(
    "val,expected",
    [
        ([1], True),
        ((1,), True),
        (set(), True),
        ("abc", False),
        (123, False),
    ],
)
def test_is_list_like(val, expected):
    assert is_list_like(val) == expected


@pytest.mark.parametrize(
    "val,expected",
    [
        ([], True),
        ((), True),
        (set(), True),
        ("", True),
        ([1], False),
        (None, False),
        (123, False),
    ],
)
def test_is_empty(val, expected):
    assert is_empty(val) == expected
