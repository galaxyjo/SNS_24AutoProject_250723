"""TaskQueueManager: Handles task queuing operations across modules."""

# modules/task_queue_mgr.py

from collections import deque
from typing import Any, Optional


class TaskQueueManager:
    """
    FIFO 기반 작업 큐 관리자.
    """

    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, item: Any) -> None:
        """
        항목을 큐에 추가합니다.
        """
        self.queue.append(item)

    def dequeue(self) -> Optional[Any]:
        """
        큐에서 항목을 제거하고 반환합니다. 큐가 비어 있으면 None 반환.
        """
        if self.queue:
            return self.queue.popleft()
        return None

    def size(self) -> int:
        """
        현재 큐의 크기를 반환합니다.
        """
        return len(self.queue)

    def is_empty(self) -> bool:
        """
        큐가 비어 있는지 여부를 반환합니다.
        """
        return not self.queue

    def clear(self) -> None:
        """
        큐를 비웁니다.
        """
        self.queue.clear()
