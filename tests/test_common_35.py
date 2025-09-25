# tests/test_common_35.py

import numpy as np
import pytest
from modules.common import common_35 as c35


def test_all_none():
    assert c35.all_none(None, None, None) is True
    assert c35.all_none(None, 1, None) is False

def test_all_not_none():
    assert c35.all_not_none(1, 2, 3) is True
    assert c35.all_not_none(1, None, 3) is False

def test_any_none():
    assert c35.any_none(None, 1, 2) is True
    assert c35.any_none(1, 2, 3) is False

def test_any_not_none():
    assert c35.any_not_none(None, None, 1) is True
    assert c35.any_not_none(None, None, None) is False

def test_apply_if_callable():
    doubler = lambda x: x * 2
    assert c35.apply_if_callable(doubler, 5) == 10  # 함수일 경우
    assert c35.apply_if_callable(3, 5) == 5          # 함수가 아닐 경우 원본 리턴

def test_cast_scalar_indexer():
    assert c35.cast_scalar_indexer(5) == 5
    assert c35.cast_scalar_indexer(np.int64(8)) == 8
    assert c35.cast_scalar_indexer("a") == "a"

def test_convert_to_list_like():
    assert c35.convert_to_list_like(None) == []
    assert c35.convert_to_list_like([1, 2]) == [1, 2]
    assert c35.convert_to_list_like((1, 2)) == [1, 2]
    assert c35.convert_to_list_like({1, 2}) in ([1, 2], [2, 1])  # set은 순서 보장 X
    assert c35.convert_to_list_like(np.array([1, 2])) == [1, 2]
    assert c35.convert_to_list_like("a") == ["a"]

def test_flatten():
    nested = [1, [2, [3, 4]], 5]
    result = list(c35.flatten(nested))
    assert result == [1, 2, 3, 4, 5]

def test_is_bool_indexer():
    assert c35.is_bool_indexer(np.array([True, False]))
    assert c35.is_bool_indexer([True, False])
    assert not c35.is_bool_indexer([1, 0])
    assert not c35.is_bool_indexer("string")

def test_pipe():
    def add(x, y): return x + y
    assert c35.pipe(3, add, 4) == 7

def test_random_state_deterministic():
    rng1 = c35.random_state(42)
    rng2 = c35.random_state(42)
    assert isinstance(rng1, np.random.Generator)
    assert isinstance(rng2, np.random.Generator)
    assert rng1.integers(0, 10) == rng2.integers(0, 10)

def test_temp_setattr():
    class Dummy:
        val = 1
    d = Dummy()
    with c35.temp_setattr(d, "val", 100):
        assert d.val == 100
    assert d.val == 1
