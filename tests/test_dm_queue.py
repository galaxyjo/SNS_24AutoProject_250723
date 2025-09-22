import pytest
import asyncio
from modules.dm.queue import (
    InboundEvent,
    ActionResult,
    DMQueue,
    _infer_action_from_event,
    _ensure_text,
    _to_action_result,
)


@pytest.mark.asyncio
async def test_enqueue_dequeue():
    q = DMQueue()
    event = InboundEvent(id="1", user_id="u1", text="hello", ts=123.4, type="dm")
    await q.enqueue(event)
    out = await q.dequeue()
    assert out == event


def test_infer_action():
    e1 = InboundEvent("1", "u", "hi", 1.0, "comment")
    e2 = InboundEvent("2", "u", "hi", 1.0, "dm")
    e3 = InboundEvent("3", "u", "hi", 1.0, "other")
    assert _infer_action_from_event(e1) == "reply"
    assert _infer_action_from_event(e2) == "send"
    assert _infer_action_from_event(e3) is None


def test_ensure_text():
    assert "도움" in _ensure_text("요청 ", "테스트")


def test_to_action_result_from_actionresult():
    e = InboundEvent("1", "u", "hi", 1.0, "dm")
    ar = ActionResult(ok=True)
    out = _to_action_result(ar, e, "send")
    assert isinstance(out, ActionResult)
    assert out.action == "send"


def test_to_action_result_from_dict():
    e = InboundEvent("1", "u", "hi", 1.0, "dm")
    out = _to_action_result({"ok": True}, e, "send")
    assert isinstance(out, ActionResult)
    assert out.data["action"] == "send"


def test_to_action_result_from_none():
    e = InboundEvent("1", "u", "hi", 1.0, "dm")
    out = _to_action_result(None, e, "send")
    assert out.ok and out.data["text"].startswith("요청")


def test_to_action_result_from_other():
    e = InboundEvent("1", "u", "hi", 1.0, "dm")
    out = _to_action_result(123, e, "send")
    assert out.ok and out.data["value"] == 123


@pytest.mark.asyncio
async def test_consume_with_sync_handler():
    q = DMQueue()
    e = InboundEvent("1", "u", "hi", 1.0, "dm")
    await q.enqueue(e)

    def handler(event):
        return {"ok": True, "text": "ok"}

    results = await q.consume(handler, stop_after=1)
    assert results[0].ok and results[0].data["text"] == "ok"


@pytest.mark.asyncio
async def test_consume_with_async_handler():
    q = DMQueue()
    e = InboundEvent("1", "u", "hi", 1.0, "comment")
    await q.enqueue(e)

    async def handler(event):
        return ActionResult(ok=True, action="reply")

    results = await q.consume(handler, stop_after=1)
    assert results[0].action == "reply"
