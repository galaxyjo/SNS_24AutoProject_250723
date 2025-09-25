# tests/test_frame_protocol.py
import pytest
from modules.common.frame_protocol import FrameProtocol, Opcode, Frame


def test_feed_and_process_text():
    proto = FrameProtocol(client=True)
    proto.feed(b"hello")
    frame = proto.process()
    assert isinstance(frame, Frame)
    assert frame.opcode == Opcode.TEXT
    assert frame.payload == "hello"
    assert frame.frame_finished
    assert frame.message_finished


def test_process_empty_buffer_returns_none():
    proto = FrameProtocol(client=True)
    result = proto.process()
    assert result is None


def test_multiple_feeds():
    proto = FrameProtocol(client=True)
    proto.feed(b"abc")
    proto.feed(b"123")
    frame = proto.process()
    assert frame.payload == "abc123"
