import queue
import threading


class EntryQueue:
    def __init__(self):
        self._queue = queue.Queue()
        self._unfinished_tasks = 0
        self._finished = threading.Condition(threading.Lock())

    def put(self, item):
        with self._finished:
            self._queue.put(item)
            self._unfinished_tasks += 1

    def get(self):
        return self._queue.get()

    def task_done(self):
        with self._finished:
            self._unfinished_tasks -= 1
            if self._unfinished_tasks <= 0:
                self._finished.notify_all()

    def join(self):
        with self._finished:
            while self._unfinished_tasks > 0:
                self._finished.wait()

    def qsize(self):
        return self._queue.qsize()

    def empty(self):
        return self._queue.empty()
