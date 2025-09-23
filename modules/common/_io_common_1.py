# -*- coding: utf-8 -*-
# Utility functions for I/O queues

from queue import Queue, Empty
from typing import Any, Optional

__all__ = ["wake_all", "try_get"]


def wake_all(queues: list[Queue]) -> None:
    """
    Put None into all queues to wake up waiting consumers.
    If a queue is closed or put fails, continue to next.
    """
    for idx, q in enumerate(queues):
        try:
            q.put_nowait(None)
            print(f"✅ Queue {idx} wake signal sent")
        except Exception as e:
            print(f"⚠️ Queue {idx} put failed: {e}")


def try_get(q: Queue, timeout: float = 1.0) -> Optional[Any]:
    """
    Try to get an item from queue with timeout.
    Return None if queue is empty.
    """
    try:
        item = q.get(timeout=timeout)
        print(f"✅ Retrieved item: {item}")
        return item
    except Empty:
        print("⚠️ Queue is empty (timeout)")
        return None


if __name__ == "__main__":
    # Quick manual test
    q1 = Queue()
    q2 = Queue()
    wake_all([q1, q2])
    print(try_get(q1))
    print(try_get(q2))
