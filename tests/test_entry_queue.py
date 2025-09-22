# tests/test_entry_queue.py
def test_init_internal_state():
    q = EntryQueue()
    assert hasattr(q, "_queue")
    assert hasattr(q, "_unfinished_tasks")
    assert hasattr(q, "_finished")
    assert isinstance(q._unfinished_tasks, int)


import threading

import pytest

from modules.queue._entry_queue import EntryQueue


def test_put_and_get():
    q = EntryQueue()
    q.put("item1")
    assert q.qsize() == 1
    assert not q.empty()

    item = q.get()
    assert item == "item1"
    assert q.qsize() == 0


def test_task_done_and_join():
    q = EntryQueue()

    def worker():
        q.put("x")
        item = q.get()
        assert item == "x"
        q.task_done()

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()

    q.join()  # block until task_done() called
    assert q.qsize() == 0


def test_multiple_tasks():
    q = EntryQueue()
    results = []

    def worker():
        while not q.empty():
            item = q.get()
            results.append(item)
            q.task_done()

    for i in range(5):
        q.put(i)

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()

    q.join()
    assert sorted(results) == [0, 1, 2, 3, 4]


def test_empty_queue():
    q = EntryQueue()
    assert q.empty()
    assert q.qsize() == 0


def test_init_condition_object_usage():
    q = EntryQueue()

    def dummy():
        with q._finished:
            q._unfinished_tasks += 1
            q._unfinished_tasks -= 1
            q._finished.notify_all()

    t = threading.Thread(target=dummy)
    t.start()
    t.join()

    with q._finished:
        assert q._unfinished_tasks == 0
