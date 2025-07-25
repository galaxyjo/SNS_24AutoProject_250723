
                await _core.cancel_shielded_checkpoint()
                return self._get_batch_protected()
                self._can_get = True
                self._lot.unpark(count=1)
              :exc:`~trio.WouldBlock` instead.
              list is always non-empty; if it would be empty we raise
              non-empty.
            assert not self._can_get
            await self._lot.park()
            else:
            finally:
            if self._lot:
            qsize=len(self._data),
            raise _core.WouldBlock
            return self._get_batch_protected()
            tasks_waiting=self._lot.statistics().tasks_waiting,
            try:
           ...
           obj = await queue.get_batch()
          ~trio.WouldBlock: if the queue is empty.
          list: A list of dequeued items, in order. On a successful call this
          list: A list of dequeued items, in order. This list is always
          obj (object): The object to enqueue.
        """
        """Attempt to get the next batch from the queue, without blocking.
        """Get the next batch from the queue, blocking as necessary.
        """Put an object into the queue, without blocking.
        """Return an :class:`UnboundedQueueStatistics` object containing debugging information."""
        """Returns the number of items currently in the queue."""
        """Returns True if the queue is empty, False otherwise.
        "0.9.0",
        # used to allow handoff from put to the first task in the lot
        )
        `issue #63 <https://github.com/python-trio/trio/issues/63>`__.
        a blocking ``put`` method, because it would never need to block.
        Args:
        await _core.checkpoint_if_cancelled()
        data = self._data.copy()
        else:
        if not self._can_get:
        if not self._data:
        instead="trio.open_memory_channel(math.inf)",
        issue=497,
        Raises:
        return await self.get_batch()
        return data
        return f"<UnboundedQueue holding {len(self._data)} items>"
        return len(self._data)
        return not self._data
        return self
        return self._get_batch_protected()
        return UnboundedQueueStatistics(
        Returns:
        self._can_get = False
        self._data.append(obj)
        self._data.clear()
        self._data: list[T] = []
        self._lot = _core.ParkingLot()
        There is some subtlety to interpreting this method's return value: see
        thing="trio.lowlevel.UnboundedQueue",
        This always succeeds, because the queue is unbounded. We don't provide
        use_triodeprecationwarning=True,
       async for batch in queue:
       while True:
      :meth:`get_batch` method.
    """
    """An object containing debugging information.
    """An unbounded queue suitable for certain unusual forms of inter-task
    "batches". If a consumer task processes each batch without yielding, then
    )
    * ``qsize``: The number of items currently in the queue.
    * ``tasks_waiting``: The number of tasks blocked on this queue's
    @_core.enable_ki_protection
    @deprecated(
    A :class:`UnboundedQueue` object can be used as an asynchronous iterator,
    are equivalent::
    async def __anext__(self) -> list[T]:
    async def get_batch(self) -> list[T]:
    communication.
    Currently each batch completely empties the queue, but `this may change in
    Currently, the following fields are defined:
    def __aiter__(self) -> Self:
    def __init__(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def __repr__(self) -> str:
    def _get_batch_protected(self) -> list[T]:
    def empty(self) -> bool:
    def get_batch_nowait(self) -> list[T]:
    def put_nowait(self, obj: T) -> None:
    def qsize(self) -> int:
    def statistics(self) -> UnboundedQueueStatistics:
    from typing_extensions import Self
    growing without bound, the consumer API is modified to dequeue items in
    has to always succeed. In order to prevent the queue backlog from actually
    in general. You should generally prefer to use a memory channel
    instead if you can.
    qsize: int
    queue's memory use, at the cost of potentially increasing system latencies
    some reason cannot be subjected to back-pressure, i.e., :meth:`put_nowait`
    tasks_waiting: int
    the future <https://github.com/python-trio/trio/issues/51>`__.
    This class is designed for use as a queue in cases where the producer for
    this helps achieve (but does not guarantee) an effective bound on the
    where each iteration returns a new batch of items. I.e., these two loops
# -*- coding: utf-8 -*-
@attrs.frozen
@final
class UnboundedQueue:
class UnboundedQueueStatistics:
from .. import _core
from .._deprecate import deprecated
from .._util import final
from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar
if TYPE_CHECKING:
import attrs
T = TypeVar("T")
