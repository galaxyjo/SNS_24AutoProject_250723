# -*- coding: utf-8 -*-
"""UnboundedQueue: 비동기 무제한 큐"""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

import attrs

from modules.core import ParkingLot, WouldBlock, checkpoint_if_cancelled

if TYPE_CHECKING:
    from typing_extensions import Self

T = TypeVar("T")


@attrs.define
class UnboundedQueueStatistics:
    """UnboundedQueue 통계 정보"""

    qsize: int
    tasks_waiting: int


@attrs.define
class UnboundedQueue(Generic[T]):
    """스레드 안전한 비동기 무제한 큐"""

    _data: list[T] = attrs.field(factory=list)
    _can_get: bool = attrs.field(default=False)
    _lot: ParkingLot = attrs.field(factory=ParkingLot)

    def __aiter__(self) -> Self:
        """비동기 반복자 시작"""
        return self

    async def __anext__(self) -> list[T]:
        """비동기 next"""
        return await self.get_batch()

    async def get_batch(self) -> list[T]:
        """큐에서 배치를 가져옴 (없으면 대기)"""
        if not self._data:
            self._can_get = False
            await checkpoint_if_cancelled()
            await self._lot.park()
        return self._get_batch_protected()

    def get_batch_nowait(self) -> list[T]:
        """즉시 배치 반환 (없으면 예외)"""
        if not self._data:
            raise WouldBlock
        return self._get_batch_protected()

    def _get_batch_protected(self) -> list[T]:
        """내부 배치 가져오기 (초기화 포함)"""
        data = self._data.copy()
        self._data.clear()
        return data

    def put_nowait(self, obj: T) -> None:
        """큐에 아이템 추가"""
        self._data.append(obj)
        self._can_get = True
        self._lot.unpark(count=1)

    def qsize(self) -> int:
        """현재 큐 크기 반환"""
        return len(self._data)

    def empty(self) -> bool:
        """비어있는지 여부"""
        return not self._data
