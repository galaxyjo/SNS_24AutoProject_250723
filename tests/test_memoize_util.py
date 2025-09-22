# tests/test_memoize_util.py

import time
from modules.common.memoize_util import memoize


def test_memoize_basic():
    calls = []

    @memoize
    def add(a, b):
        calls.append(1)
        return a + b

    assert add(1, 2) == 3
    assert add(1, 2) == 3
    assert len(calls) == 1  # Only computed once


def test_memoize_multiple_args():
    calls = []

    @memoize
    def multiply(a, b, c):
        calls.append(1)
        return a * b * c

    assert multiply(2, 3, 4) == 24
    assert multiply(2, 3, 4) == 24
    assert len(calls) == 1


def test_memoize_diff_args():
    calls = []

    @memoize
    def subtract(a, b):
        calls.append(1)
        return a - b

    assert subtract(5, 2) == 3
    assert subtract(4, 1) == 3
    assert subtract(5, 2) == 3
    assert len(calls) == 2


def test_memoize_performance():
    @memoize
    def slow_add(a, b):
        time.sleep(0.1)
        return a + b

    start = time.time()
    assert slow_add(10, 20) == 30
    first = time.time() - start

    start = time.time()
    assert slow_add(10, 20) == 30
    second = time.time() - start

    assert second < first
