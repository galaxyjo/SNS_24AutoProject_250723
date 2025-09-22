# modules/core/parking_lot.py


class ParkingLot:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)
        return None

    def peek(self):
        if self._queue:
            return self._queue[0]
        return None

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)
