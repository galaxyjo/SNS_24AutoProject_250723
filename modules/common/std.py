# modules/common/std.py
import queue


class Comparable:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if not isinstance(other, Comparable):
            return NotImplemented
        return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, Comparable):
            return NotImplemented
        return self.value == other.value


class tqdm:
    def __init__(self, iterable=None, total=None, desc=None):
        self.iterable = iterable
        self.total = total or (len(iterable) if iterable is not None else 0)
        self.desc = desc
        self.count = 0

    def __iter__(self):
        for item in self.iterable:
            self.count += 1
            self.display()
            yield item

    def display(self):
        print(f"{self.desc or ''} [{self.count}/{self.total}]")


if not hasattr(queue, "SimpleQueue"):
    queue.SimpleQueue = queue.Queue
