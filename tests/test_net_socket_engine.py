# tests/test_net_socket_engine.py
import pytest
from modules.common.net_socket_engine import NetSocketEngine


class DummySocket:
    def __init__(self):
        self.sent = []
        self.closed = False
        self.to_receive = b"reply"

    def connect(self, addr):
        self.addr = addr

    def sendall(self, data):
        self.sent.append(data)

    def recv(self, bufsize):
        return self.to_receive

    def close(self):
        self.closed = True


def test_connect_and_send(monkeypatch):
    engine = NetSocketEngine("example.com", 1234)
    dummy = DummySocket()
    engine.sock = dummy
    engine.send(b"hello")
    assert b"hello" in dummy.sent


def test_send_without_connect_raises():
    engine = NetSocketEngine()
    with pytest.raises(ConnectionError):
        engine.send(b"data")


def test_send_with_invalid_type(monkeypatch):
    engine = NetSocketEngine()
    engine.sock = DummySocket()
    with pytest.raises(TypeError):
        engine.send("not_bytes")  # type: ignore


def test_receive_and_close():
    engine = NetSocketEngine()
    dummy = DummySocket()
    engine.sock = dummy
    result = engine.receive()
    assert result == b"reply"
    engine.close()
    assert dummy.closed
