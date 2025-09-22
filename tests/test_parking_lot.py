# tests/test_parking_lot.py

from modules.core.parking_lot import ParkingLot


def test_enqueue_and_dequeue():
    lot = ParkingLot()
    lot.enqueue("A")
    lot.enqueue("B")
    assert lot.dequeue() == "A"
    assert lot.dequeue() == "B"
    assert lot.dequeue() is None


def test_peek_and_is_empty():
    lot = ParkingLot()
    assert lot.is_empty()
    lot.enqueue("X")
    assert not lot.is_empty()
    assert lot.peek() == "X"


def test_size():
    lot = ParkingLot()
    assert lot.size() == 0
    lot.enqueue(1)
    lot.enqueue(2)
    assert lot.size() == 2
