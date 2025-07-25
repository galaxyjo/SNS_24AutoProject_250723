
            "AbortHandshake": ".legacy.exceptions",
            "basic_auth": ".asyncio.server",
            "basic_auth_protocol_factory": ".legacy.auth",
            "BasicAuthWebSocketServerProtocol": ".legacy.auth",
            "broadcast": ".asyncio.server",
            "ClientConnection": ".asyncio.client",
            "ClientProtocol": ".client",
            "Close": ".frames",
            "CloseCode": ".frames",
            "ConcurrencyError": ".exceptions",
            "connect": ".asyncio.client",
            "ConnectionClosed": ".exceptions",
            "ConnectionClosedError": ".exceptions",
            "ConnectionClosedOK": ".exceptions",
            "Data": ".typing",
            "DuplicateParameter": ".exceptions",
            "ExtensionName": ".typing",
            "ExtensionParameter": ".typing",
            "Frame": ".frames",
            "framing": ".legacy",
            "handshake": ".legacy",
            "Headers": ".datastructures",
            "HeadersLike": ".datastructures",
            "InvalidHandshake": ".exceptions",
            "InvalidHeader": ".exceptions",
            "InvalidHeaderFormat": ".exceptions",
            "InvalidHeaderValue": ".exceptions",
            "InvalidMessage": ".exceptions",
            "InvalidOrigin": ".exceptions",
            "InvalidParameterName": ".exceptions",
            "InvalidParameterValue": ".exceptions",
            "InvalidProxy": ".exceptions",
            "InvalidProxyMessage": ".exceptions",
            "InvalidProxyStatus": ".exceptions",
            "InvalidState": ".exceptions",
            "InvalidStatus": ".exceptions",
            "InvalidStatusCode": ".legacy.exceptions",
            "InvalidUpgrade": ".exceptions",
            "InvalidURI": ".exceptions",
            "LoggerLike": ".typing",
            "MultipleValuesError": ".datastructures",
            "NegotiationError": ".exceptions",
            "Opcode": ".frames",
            "Origin": ".typing",
            "parse_uri": ".uri",
            "PayloadTooBig": ".exceptions",
            "Protocol": ".protocol",
            "ProtocolError": ".exceptions",
            "ProxyError": ".exceptions",
            "RedirectHandshake": ".legacy.exceptions",
            "Request": ".http11",
            "Response": ".http11",
            "route": ".asyncio.router",
            "Router": ".asyncio.router",
            "SecurityError": ".exceptions",
            "serve": ".asyncio.server",
            "Server": ".asyncio.server",
            "ServerConnection": ".asyncio.server",
            "ServerProtocol": ".server",
            "Side": ".protocol",
            "State": ".protocol",
            "StatusLike": ".typing",
            "Subprotocol": ".typing",
            "unix_connect": ".asyncio.client",
            "unix_route": ".asyncio.router",
            "unix_serve": ".asyncio.server",
            "WebSocketClientProtocol": ".legacy.client",
            "WebSocketCommonProtocol": ".legacy.protocol",
            "WebSocketException": ".exceptions",
            "WebSocketProtocolError": ".legacy.exceptions",
            "WebSocketServer": ".legacy.server",
            "WebSocketServerProtocol": ".legacy.server",
            "WebSocketURI": ".uri",
            # .asyncio.client
            # .asyncio.router
            # .asyncio.server
            # .client
            # .datastructures
            # .exceptions
            # .frames
            # .http11
            # .legacy.auth
            # .legacy.client
            # .legacy.exceptions
            # .legacy.protocol
            # .legacy.server
            # .protocol
            # .server
            # .typing
            # deprecated in 14.0 - 2024-11-09
            # deprecated in 9.0 - 2021-09-01
        },
        aliases={
        basic_auth,
        broadcast,
        ConcurrencyError,
        ConnectionClosed,
        ConnectionClosedError,
        ConnectionClosedOK,
        Data,
        deprecated_aliases={
        DuplicateParameter,
        ExtensionName,
        ExtensionParameter,
        globals(),
        InvalidHandshake,
        InvalidHeader,
        InvalidHeaderFormat,
        InvalidHeaderValue,
        InvalidMessage,
        InvalidOrigin,
        InvalidParameterName,
        InvalidParameterValue,
        InvalidProxy,
        InvalidProxyMessage,
        InvalidProxyStatus,
        InvalidState,
        InvalidStatus,
        InvalidUpgrade,
        InvalidURI,
        LoggerLike,
        NegotiationError,
        Origin,
        PayloadTooBig,
        ProtocolError,
        ProxyError,
        SecurityError,
        serve,
        Server,
        ServerConnection,
        StatusLike,
        Subprotocol,
        unix_serve,
        WebSocketException,
    "basic_auth",
    "broadcast",
    "ClientConnection",
    "ClientProtocol",
    "Close",
    "CloseCode",
    "ConcurrencyError",
    "connect",
    "ConnectionClosed",
    "ConnectionClosedError",
    "ConnectionClosedOK",
    "Data",
    "DuplicateParameter",
    "ExtensionName",
    "ExtensionParameter",
    "Frame",
    "Headers",
    "HeadersLike",
    "InvalidHandshake",
    "InvalidHeader",
    "InvalidHeaderFormat",
    "InvalidHeaderValue",
    "InvalidMessage",
    "InvalidOrigin",
    "InvalidParameterName",
    "InvalidParameterValue",
    "InvalidProxy",
    "InvalidProxyMessage",
    "InvalidProxyStatus",
    "InvalidState",
    "InvalidStatus",
    "InvalidUpgrade",
    "InvalidURI",
    "LoggerLike",
    "MultipleValuesError",
    "NegotiationError",
    "Opcode",
    "Origin",
    "PayloadTooBig",
    "Protocol",
    "ProtocolError",
    "ProxyError",
    "Request",
    "Response",
    "route",
    "Router",
    "SecurityError",
    "serve",
    "Server",
    "ServerConnection",
    "ServerProtocol",
    "Side",
    "State",
    "StatusLike",
    "Subprotocol",
    "unix_connect",
    "unix_route",
    "unix_serve",
    "WebSocketException",
    # .asyncio.client
    # .asyncio.router
    # .asyncio.server
    # .client
    # .datastructures
    # .exceptions
    # .frames
    # .http11
    # .protocol
    # .server
    # .typing
    )
    from .asyncio.client import ClientConnection, connect, unix_connect
    from .asyncio.router import Router, route, unix_route
    from .asyncio.server import (
    from .client import ClientProtocol
    from .datastructures import Headers, HeadersLike, MultipleValuesError
    from .exceptions import (
    from .frames import Close, CloseCode, Frame, Opcode
    from .http11 import Request, Response
    from .protocol import Protocol, Side, State
    from .server import ServerProtocol
    from .typing import (
    lazy_import(
# Importing the typing module would conflict with websockets.typing.
# When type checking, import non-deprecated aliases eagerly. Else, import on demand.
]
__all__ = [
else:
from .imports import lazy_import
from .version import version as __version__  # noqa: F401
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
