# tests/test_handshake.py
import pytest
from modules.common.handshake import Handshake, HandshakeError


def test_handshake_success():
    h = Handshake(client=True)
    proto = h.initiate(["json", "xml"])
    assert proto == "json"
    assert h.is_complete()


def test_handshake_fail():
    h = Handshake(client=False)
    with pytest.raises(HandshakeError):
        h.initiate([])


def test_handshake_reset():
    h = Handshake(client=True)
    h.initiate(["proto1"])
    assert h.is_complete()
    h.reset()
    assert not h.is_complete()
