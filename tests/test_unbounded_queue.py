# tests/test_unbounded_queue.py

import asyncio
from unittest.mock import MagicMock

import pytest

from modules.core import WouldBlock
from modules.queue._unbounded_queue import UnboundedQueue


@pytest.fixture
def queue_with_mock_lot(monkeypatch):
    queue = UnboundedQueue()

    # ParkingLot의 unpark 모의 정의
    mock_lot = MagicMock()
    queue._lot = mock_lot
    return queue


@pytest.mark.asyncio
async def test_put_and_get_batch(queue_with_mock_lot):
    queue = queue_with_mock_lot
    queue.put_nowait("item1")
    queue.put_nowait("item2")

    batch = await queue.get_batch()
    assert batch == ["item1", "item2"]
    assert queue.empty()


def test_put_and_get_batch_nowait(queue_with_mock_lot):
    queue = queue_with_mock_lot
    queue.put_nowait("itemX")
    queue.put_nowait("itemY")

    batch = queue.get_batch_nowait()
    assert batch == ["itemX", "itemY"]
    assert queue.empty()


def test_get_batch_nowait_raises():
    queue = UnboundedQueue()
    with pytest.raises(WouldBlock):
        queue.get_batch_nowait()


def test_qsize_and_empty(queue_with_mock_lot):
    queue = queue_with_mock_lot
    assert queue.empty()
    assert queue.qsize() == 0

    queue.put_nowait("one")
    queue.put_nowait("two")

    assert not queue.empty()
    assert queue.qsize() == 2


@pytest.mark.asyncio
async def test_aiter_anext(queue_with_mock_lot):
    queue = queue_with_mock_lot
    queue.put_nowait("A")
    queue.put_nowait("B")

    async for batch in queue:
        assert batch == ["A", "B"]
        break  # 무한 루프 방지


@pytest.mark.asyncio
async def test_get_batch_when_empty(monkeypatch):
    queue = UnboundedQueue()

    called = {"checkpoint": False, "park": False}

    # checkpoint_if_cancelled 모킹
    async def fake_checkpoint():
        called["checkpoint"] = True

    # ParkingLot.park 모킹 + CancelledError 강제 발생
    class FakeLot:
        async def park(self):
            called["park"] = True
            raise asyncio.CancelledError()

    monkeypatch.setattr(
        "modules.queue._unbounded_queue.checkpoint_if_cancelled", fake_checkpoint
    )
    queue._lot = FakeLot()

    with pytest.raises(asyncio.CancelledError):
        await queue.get_batch()

    assert called["checkpoint"] is True
    assert called["park"] is True


@pytest.mark.asyncio
async def test_get_batch_sets_can_get_false_normal(monkeypatch):
    queue = UnboundedQueue()

    # 가짜 대기 함수 - 실제 대기 안 하고 바로 return
    async def fake_checkpoint():
        pass

    class FakeLot:
        async def park(self):
            pass  # cancel 없이 정상 종료

    monkeypatch.setattr(
        "modules.queue._unbounded_queue.checkpoint_if_cancelled", fake_checkpoint
    )
    queue._lot = FakeLot()

    # 실행 전 상태
    assert queue._can_get is False
    assert queue.empty()

    # 직접 실행 (비동기)
    result = await queue.get_batch()
    assert result == []
    assert queue._can_get is False
