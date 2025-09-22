import time
import pytest
from modules.dm.queue import InboundEvent


def test_inbound_event_instantiation():
    event = InboundEvent(
        id="ev001",
        user_id="user123",
        text="hello world",
        ts=1620000000.0,
        type="mention",
    )
    assert event.id == "ev001"
    assert event.user_id == "user123"
    assert event.text == "hello world"
    assert event.ts == 1620000000.0
    assert event.type == "mention"


def test_inbound_event_defaults():
    now = time.time()
    event = InboundEvent(
        id="ev002", user_id="user999", text="just testing", ts=now, type="comment"
    )
    assert isinstance(event.ts, float)
    assert event.type in ["comment", "mention"]


def test_inbound_event_str_repr():
    event = InboundEvent(
        id="ev003", user_id="tester", text="test text", ts=1234567890.0, type="comment"
    )
    assert "ev003" in str(event)
    assert "tester" in str(event)
