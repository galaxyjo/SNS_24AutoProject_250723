# tests/test_random_util.py

import pytest
from modules.common import random_util


def test_random_int():
    result = random_util.random_int(1, 10)
    assert 1 <= result <= 10


def test_random_float():
    result = random_util.random_float(1.0, 2.0)
    assert 1.0 <= result <= 2.0


def test_random_choice():
    seq = [1, 2, 3]
    assert random_util.random_choice(seq) in seq
    assert random_util.random_choice([]) is None


def test_random_string():
    result = random_util.random_string(12)
    assert isinstance(result, str)
    assert len(result) == 12
