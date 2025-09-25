# tests/test_std.py
import pytest
import queue
from modules.common.std import Comparable, tqdm


def test_comparable_operations():
    a, b = Comparable(1), Comparable(2)
    assert a < b
    assert not (a == b)
    assert (a == Comparable(1))
    assert (a != b)


def test_comparable_invalid_comparison():
    a = Comparable(1)
    assert (a.__eq__("x") == NotImplemented)
    assert (a.__lt__("x") == NotImplemented)


def test_tqdm_iteration_and_display(capsys):
    items = list(tqdm(iterable=[1, 2, 3], desc="test"))
    assert items == [1, 2, 3]
    captured = capsys.readouterr()
    assert "test" in captured.out
    assert "[3/3]" in captured.out


def test_simplequeue_patch(monkeypatch):
    if hasattr(queue, "SimpleQueue"):
        delattr(queue, "SimpleQueue")
    from importlib import reload
    import modules.common.std as std
    reload(std)
    assert hasattr(queue, "SimpleQueue")
