import pytest
from modules.common import random_custom


def test_randint():
    result = random_custom.randint(1, 10)
    assert 1 <= result <= 10


def test_randrange_single():
    result = random_custom.randrange(5)
    assert 0 <= result < 5


def test_randrange_double():
    result = random_custom.randrange(10, 20)
    assert 10 <= result < 20


def test_choice():
    result = random_custom.choice(["apple", "banana", "cherry"])
    assert result in ["apple", "banana", "cherry"]


def test_sample():
    result = random_custom.sample([1, 2, 3, 4, 5], 3)
    assert len(result) == 3
    assert all(x in [1, 2, 3, 4, 5] for x in result)


def test_shuffle():
    x = [1, 2, 3, 4]
    original = x[:]
    random_custom.shuffle(x)
    assert sorted(x) == sorted(original)


def test_getrandbits():
    result = random_custom.getrandbits(8)
    assert isinstance(result, int)
    assert 0 <= result < 256
