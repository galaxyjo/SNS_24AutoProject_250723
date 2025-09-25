# modules/common/queue_utils.py
# 출처: _io_common_1.py 기반 통합 리팩토링

from queue import Queue, Empty
from typing import Any, Optional


def wake_all(queues: list[Queue]) -> None:
    """
    모든 Queue에 None을 넣어 대기 중인 소비자(watcher)를 깨움
    """
    for idx, q in enumerate(queues):
        try:
            q.put_nowait(None)
            print(f"✅ Queue {idx} wake signal sent")
        except Exception as e:
            print(f"⚠️ Queue {idx} put failed: {e}")


def try_get(q: Queue, timeout: float = 1.0) -> Optional[Any]:
    """
    지정된 시간 안에 Queue에서 값을 가져옴
    실패 시 None 반환
    """
    try:
        item = q.get(timeout=timeout)
        print(f"✅ Retrieved item: {item}")
        return item
    except Empty:
        print("⚠️ Queue is empty (timeout)")
        return None
