# tests/test_proj_concurrent.py (수정/디버깅 버전)
import pytest
from modules.common import proj_concurrent as pc

# top-level functions for pickling in ProcessPoolExecutor
def cube(x):
    return x ** 3

def square(x):
    return x * x

def identity(x):
    return x

def test_thread_map_simple():
    result = pc.thread_map(square, range(5))
    assert result == [0, 1, 4, 9, 16]


def test_process_map_simple():
    result = pc.process_map(cube, range(4))
    assert result == [0, 1, 8, 27]


def test_chunksize_warning(monkeypatch):
    called = {}

    def dummy_warn(msg, category, stacklevel):
        called["msg"] = msg
        called["category"] = category
        called["stacklevel"] = stacklevel

    monkeypatch.setattr("warnings.warn", dummy_warn)
    iterables = [range(2000)]
    pc._executor_map(pc.ThreadPoolExecutor, identity, *iterables)
    assert "Iterable length > 1000" in called["msg"]
