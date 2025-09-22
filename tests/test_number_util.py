# tests/test_number_util.py

import pytest
from modules.common import number_util as nu


def test_clamp_basic():
    assert nu.clamp(5, 1, 10) == 5
    assert nu.clamp(-5, 0, 10) == 0
    assert nu.clamp(15, 0, 10) == 10


def test_round_to():
    assert nu.round_to(3.14159, 2) == 3.14
    assert nu.round_to(2.5) == 2
    assert nu.round_to(-2.5) == -2


def test_safe_int():
    assert nu.safe_int("42") == 42
    assert nu.safe_int("3.14") == 3
    assert nu.safe_int(7.9) == 7
    assert nu.safe_int(None) is None
    assert nu.safe_int("abc") is None


def test_safe_float():
    assert nu.safe_float("3.14") == 3.14
    assert nu.safe_float(5) == 5.0
    assert nu.safe_float(None) is None
    assert nu.safe_float("not a number") is None


def test_is_numeric():
    assert nu.is_numeric("123.45")
    assert nu.is_numeric(42)
    assert nu.is_numeric(3.14)
    assert not nu.is_numeric("abc")
    assert not nu.is_numeric(None)
