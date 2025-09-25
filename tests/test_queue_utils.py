# tests/test_queue_utils.py

from modules.common.queue_utils import wake_all, try_get
from queue import Queue


def test_wake_all_and_try_get():
    q1 = Queue()
    q2 = Queue()
    wake_all([q1, q2])

    assert try_get(q1, timeout=0.1) is None
    assert try_get(q2, timeout=0.1) is None


def test_try_get_with_item():
    q = Queue()
    q.put("hello")
    result = try_get(q)
    assert result == "hello"
