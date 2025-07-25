
    "CLIENT",
    "CLOSED",
    "Connection",
    "ConnectionClosed",
    "Data",
    "DONE",
    "EndOfMessage",
    "ERROR",
    "Event",
    "IDLE",
    "InformationalResponse",
    "LocalProtocolError",
    "MUST_CLOSE",
    "NEED_DATA",
    "PAUSED",
    "ProtocolError",
    "RemoteProtocolError",
    "Request",
    "Response",
    "SEND_BODY",
    "SEND_RESPONSE",
    "SERVER",
    "SWITCHED_PROTOCOL",
    CLIENT,
    CLOSED,
    ConnectionClosed,
    Data,
    DONE,
    EndOfMessage,
    ERROR,
    Event,
    IDLE,
    InformationalResponse,
    MUST_CLOSE,
    Request,
    Response,
    SEND_BODY,
    SEND_RESPONSE,
    SERVER,
    SWITCHED_PROTOCOL,
# A highish-level implementation of the HTTP/1.1 wire protocol (RFC 7230),
# but at least it gets you out of dealing with the wire itself.
# class). There's still a bunch of subtle details you need to get right if you
# containing no networking code at all, loosely modelled on hyper-h2's generic
# implementation of HTTP/2 (and in particular the h2.connection.H2Connection
# semantics to check that what you're asking to write to the wire is sensible,
# want to make this actually useful, because it doesn't implement all the
)
__all__ = (
from h11._connection import Connection, NEED_DATA, PAUSED
from h11._events import (
from h11._state import (
from h11._util import LocalProtocolError, ProtocolError, RemoteProtocolError
from h11._version import __version__
PRODUCT_ID = "python-h11/" + __version__
