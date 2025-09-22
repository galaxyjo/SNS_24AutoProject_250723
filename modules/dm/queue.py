# mypy: allow-untyped-defs
import asyncio
import inspect
import logging
from dataclasses import dataclass
from typing import Any, List, Optional, Union

from collections.abc import Callable, Coroutine

logger = logging.getLogger("modules.dm.queue")


# --- 모델 --------------------------------------------------------------------
@dataclass
class InboundEvent:
    id: str
    user_id: str
    text: str
    ts: float
    type: str
    metadata: dict | None = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class ActionResult:
    ok: bool
    action: str | None = None
    data: dict | None = None
    error: str | None = None


Handler = Callable[
    [InboundEvent],
    Union[
        ActionResult,
        dict,
        Coroutine[Any, Any, Union[ActionResult, dict, Any]],
        Any,
    ],
]


# --- 유틸 --------------------------------------------------------------------
def _infer_action_from_event(event: InboundEvent) -> str | None:
    """이벤트 타입 기반 기본 action 추론"""
    t = (event.type or "").lower()
    if t in ("comment", "post_comment"):
        return "reply"
    if t in ("dm", "message", "inbox"):
        return "send"
    return None


def _ensure_text(default_prefix: str, event_text: str) -> str:
    """항상 '도움'을 포함한 안내 문구를 생성"""
    return f"{default_prefix}도움: {event_text}"


def _to_action_result(
    x: Any, event: InboundEvent, inferred_action: str | None
) -> ActionResult:
    """handler 결과를 ActionResult로 일관성 있게 변환"""
    if isinstance(x, ActionResult):
        if not x.action and inferred_action:
            return ActionResult(
                ok=x.ok, action=inferred_action, data=x.data, error=x.error
            )
        return x

    if isinstance(x, dict):
        base = dict(x)
        if not base.get("action") and inferred_action:
            base["action"] = inferred_action
        if "text" not in base:
            base["text"] = _ensure_text("요청 ", event.text)
        base.setdefault("id", event.id)
        base.setdefault("user_id", event.user_id)
        base.setdefault("type", event.type)
        base.setdefault("ts", event.ts)
        ok_val = bool(base.get("ok", True))
        return ActionResult(
            ok=ok_val, action=base.get("action"), data=base, error=base.get("error")
        )

    if x is None:
        return ActionResult(
            ok=True,
            action=inferred_action,
            data={
                "text": _ensure_text("요청 ", event.text),
                "id": event.id,
                "user_id": event.user_id,
                "type": event.type,
                "ts": event.ts,
            },
            error=None,
        )

    return ActionResult(
        ok=bool(x),
        action=inferred_action,
        data={
            "value": x,
            "text": _ensure_text("요청 ", event.text),
            "id": event.id,
            "user_id": event.user_id,
            "type": event.type,
            "ts": event.ts,
        },
        error=None,
    )


# --- 큐 ----------------------------------------------------------------------
class DMQueue:
    """InboundEvent 비동기 큐"""

    def __init__(self) -> None:
        self._q: "asyncio.Queue[InboundEvent]" = asyncio.Queue()

    async def enqueue(self, event: InboundEvent) -> None:
        await self._q.put(event)

    async def dequeue(self) -> InboundEvent:
        return await self._q.get()

    async def consume(
        self, handler: Handler, *, stop_after: int | None = None
    ) -> list[ActionResult]:
        """
        큐에서 이벤트를 꺼내 handler에 전달하고 ActionResult로 통일
        - handler가 ActionResult → 그대로
        - awaitable → await 후 동일 처리
        - dict/None/임의 값 → _to_action_result 로 변환
        """
        results: list[ActionResult] = []
        processed = 0
        while True:
            if stop_after is not None and processed >= stop_after:
                break

            event = await self._q.get()
            logger.info("consume id=%s type=%s", event.id, event.type)

            maybe = handler(event)
            if inspect.isawaitable(maybe):
                maybe = await maybe

            if isinstance(maybe, ActionResult):
                res = maybe
            else:
                inferred = _infer_action_from_event(event)
                res = _to_action_result(maybe, event=event, inferred_action=inferred)

            results.append(res)
            processed += 1
            self._q.task_done()

            if stop_after is None and self._q.empty():
                break

        return results


__all__ = ["InboundEvent", "ActionResult", "DMQueue"]
