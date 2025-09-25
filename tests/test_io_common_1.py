import pytest
from queue import Queue
from modules.common import _io_common_1


def test_wake_all_puts_none():
    q1, q2 = Queue(), Queue()
    _io_common_1.wake_all([q1, q2])
    assert q1.get() is None, "Queue 1 did not receive wake signal"
    assert q2.get() is None, "Queue 2 did not receive wake signal"


def test_try_get_returns_item():
    q = Queue()
    q.put("data")
    result = _io_common_1.try_get(q)
    assert result == "data", "Did not retrieve expected item"


def test_try_get_returns_none_on_empty():
    q = Queue()
    result = _io_common_1.try_get(q, timeout=0.1)
    assert result is None, "Expected None for empty queue"


def test_wake_all_handles_exceptions_gracefully():
    class FakeQueue:
        def put_nowait(self, item):
            raise RuntimeError("Simulated failure")

    q = FakeQueue()
    _io_common_1.wake_all([q])  # Should not raise


def test_try_get_timeout_behavior():
    q = Queue()
    result = _io_common_1.try_get(q, timeout=0.05)
    assert result is None, "Expected None when queue is empty and timeout short"
