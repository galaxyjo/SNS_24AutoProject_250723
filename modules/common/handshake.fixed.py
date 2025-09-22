
has_body = False,
                                headers = list(event.headers),
                                status_code = event.status_code,
                            )
                            has_body=True,
                            headers=list(event.headers),
                            RejectConnection(
                            status_code=event.status_code,
                        )
                        accepts[extension.name] = True
                        extensions.append(bname)
                        RejectConnection(
                        RejectData(data=event.data, body_finished=False)
                        self._events.append(
                        self._events.append(self._establish_client_connection(event))
                        self._state = ConnectionState.CLOSED
                    "Bad HTTP message", event_hint=RejectConnection()
                    (", ".join(request.subprotocols)).encode("ascii"),
                    )
                    accepts[extension.name] = accept.encode("ascii")
                    b"Sec-WebSocket-Protocol",
                    else:
                    event_hint=RejectConnection(),
                    extensions.append(b"%s" % (name_bytes))
                    extensions.append(b"%s; %s" % (bname, params.encode("ascii")))
                    extensions.append(b"%s; %s" % (name_bytes, params))
                    f"unrecognized subprotocol {subprotocol}",
                    headers=[(b"Sec-WebSocket-Version", WEBSOCKET_VERSION)],
                    if accept:
                    if event.status_code == 101:
                    if params:
                    self._events.append(
                    self._events.append(RejectData(data=b"", body_finished=True))
                    self._events.append(self._process_connection_request(event))
                    self._state = ConnectionState.CLOSED
                    self._state = ConnectionState.REJECTING
                    status_code=426 if version else 400,
                "Cannot initiate an upgrade connection when acting as the client"
                "Connection cannot be rejected in state %s" % self.state
                "Missing header, 'Connection: Upgrade'", event_hint=RejectConnection()
                "Missing header, 'Host'", event_hint=RejectConnection()
                "Missing header, 'Sec-WebSocket-Key'", event_hint=RejectConnection()
                "Missing header, 'Sec-WebSocket-Version'",
                "Missing header, 'Upgrade: WebSocket'", event_hint=RejectConnection()
                "Request method must be GET", event_hint=RejectConnection()
                (
                (b"Sec-WebSocket-Protocol", event.subprotocol.encode("ascii"))
                )
                ),
                accept = extension.accept(offer)
                accept = value
                accepts = split_comma_header(value)
                assert isinstance(e, Extension)
                assert params
                bname = name.encode("ascii")
                break
                cast(Sequence[str], self._initiating_request.extensions),
                connection_tokens = split_comma_header(value)
                continue  # Skip appending to headers
                elif accept is not None:
                elif isinstance(event, h11.Data):
                elif isinstance(event, h11.EndOfMessage):
                elif isinstance(event, h11.Response):
                else:
                event = self._h11_connection.next_event()
                event.extensions,
                event_hint=RejectConnection(
                extension.finalize(accept)
                extensions.append(extension)
                extensions.append(name_bytes)
                extensions.extend(split_comma_header(value))
                f"Cannot send rejection data in state {self.state}"
                f"Event {event} cannot be sent during the handshake"
                f"unrecognized extension {name}", event_hint=RejectConnection()
                headers.append((b"Sec-WebSocket-Extensions", accepts))
                headers.append((b"Sec-WebSocket-Extensions", b", ".join(extensions)))
                host = value.decode("idna")
                if isinstance(accept, bool):
                if isinstance(event, h11.InformationalResponse):
                if isinstance(event, h11.Request):
                if isinstance(params, bool):
                if params == b"":
                isinstance(event, h11.ConnectionClosed)
                key = value
                offers[e.name] = e.offer()
                or event is h11.NEED_DATA
                or event is h11.PAUSED
                raise LocalProtocolError(f"unexpected subprotocol {event.subprotocol}")
                raise RemoteProtocolError(
                subprotocol = value.decode("ascii")
                subprotocols.extend(split_comma_header(value))
                upgrade = value
                version = value
            (b"Connection", b"Upgrade"),
            (b"Host", request.host.encode("idna")),
            (b"Sec-WebSocket-Accept", accept_token),
            (b"Sec-WebSocket-Key", self._nonce),
            (b"Sec-WebSocket-Version", WEBSOCKET_VERSION),
            (b"Upgrade", b"WebSocket"),
            )
            ):
            accepts = server_extensions_handshake(
            accepts, cast(Sequence[Extension], self._initiating_request.extensions)
            ConnectionType.CLIENT if self.client else ConnectionType.SERVER,
            data += self._accept(event)
            data += self._h11_connection.send(h11.EndOfMessage()) or b""
            data += self._initiate_connection(event)
            data += self._reject(event)
            data += self._send_reject_data(event)
            elif name == b"host":
            elif name == b"sec-websocket-accept":
            elif name == b"sec-websocket-extensions":
            elif name == b"sec-websocket-key":
            elif name == b"sec-websocket-protocol":
            elif name == b"sec-websocket-version":
            elif name == b"upgrade":
            else:
            event.extensions,
            except h11.RemoteProtocolError:
            extensions = []
            extensions,
            extensions=extensions,
            extensions=extensions, extra_headers=headers, subprotocol=subprotocol
            extra_headers=headers,
            for e in request.extensions:
            for name, params in offers.items():
            headers.append(
            headers.append((b"content-length", b"0"))
            headers.append((name, value))
            headers=headers + request.extra_headers,
            host=host,
            if (
            if accepts:
            if event.subprotocol not in self._initiating_request.subprotocols:
            if extension.name == name:
            if extensions:
            if isinstance(params, bool):
            if name == b"connection":
            if self.client:
            if subprotocol not in self._initiating_request.subprotocols:
            method=b"GET",
            name = name.lower()
            name_bytes = name.encode("ascii")
            offers: Dict[str, Union[str, bool]] = {}
            raise LocalProtocolError(
            raise RemoteProtocolError(
            raise RemoteProtocolError("Bad accept token", event_hint=RejectConnection())
            self.__class__.__name__, self.client, self.state
            self._h11_connection = h11.Connection(h11.CLIENT)
            self._h11_connection = h11.Connection(h11.SERVER)
            self._h11_connection.trailing_data[0],
            self._state = ConnectionState.CLOSED
            status_code=101, headers=headers + event.extra_headers
            subprotocols=subprotocols,
            target=event.target.decode("ascii"),
            target=request.target.encode("ascii"),
            token.lower() == "upgrade" for token in connection_tokens
            try:
            yield self._events.popleft()
        """
        """Initiate an upgrade connection.
        """Receive data from the remote.
        """Return a generator that provides any events that have been generated
        """Return the established connection.
        """Send an event to the remote.
        # _accept is always called after _process_connection_request.
        # _establish_client_connection is always called after _initiate_connection.
        )
        ):
        :param bytes data: Data received from the WebSocket peer.
        :param list headers: HTTP headers represented as a list of 2-tuples.
        :param str path: A URL path.
        :returns: a generator that yields H11 events.
        :returns: Data to send to the WebSocket peer.
        :rtype: bytes
        :rtype: h11.Connection
        ]
        A list of events that the remote peer triggered by sending
        a LocalProtocolError if the event is not valid given the
        accept = None
        accept_token = generate_accept_token(nonce)
        accept_token = generate_accept_token(self._nonce)
        accepts: List[str] = []
        assert self._initiating_request is not None
        assert self._nonce is not None
        by protocol activity.
        connection_tokens = None
        data = b""
        data = self._h11_connection.send(h11.Data(data=event.data)) or b""
        data = self._h11_connection.send(response) or b""
        elif isinstance(event, AcceptConnection):
        elif isinstance(event, RejectConnection):
        elif isinstance(event, RejectData):
        else:
        established.
        extensions = client_extensions_handshake(
        extensions: List[bytes] = []
        extensions: List[str] = []
        for extension in supported:
        for name, params in accepts.items():
        for name, value in event.headers:
        h11_client = h11.Connection(h11.CLIENT)
        headers = [
        headers = list(event.headers)
        headers: Headers = []
        host = None
        if accept != accept_token:
        if connection_tokens is None or not any(
        if event.body_finished:
        if event.extensions:
        if event.method != b"GET":
        if event.subprotocol is not None:
        if host is None:
        if isinstance(event, Request):
        if key is None:
        if not event.has_body:
        if request.extensions:
        if request.subprotocols:
        if self.client:
        if self.state != ConnectionState.CONNECTING:
        if self.state != ConnectionState.REJECTING:
        if subprotocol is not None:
        if upgrade.lower() != b"websocket":
        if version != WEBSOCKET_VERSION:
        key = None
        LocalProtocolError if the connection has not yet been
        name = accept.split(";", 1)[0].strip()
        name = offer.split(";", 1)[0].strip()
        nonce = request_headers[b"sec-websocket-key"]
        parsed.
        request_headers = normed_header_dict(self._initiating_request.extra_headers)
        response = h11.InformationalResponse(
        response = h11.Response(status_code=event.status_code, headers=headers)
        return "{}(client={}, state={})".format(
        return AcceptConnection(
        return b", ".join(extensions)
        return data
        return self._connection
        return self._h11_connection.send(response) or b""
        return self._h11_connection.send(upgrade) or b""
        return self._initiating_request
        return self._state
        self, event: h11.InformationalResponse
        self, event: h11.Request
        self, headers: Headers, path: Union[bytes, str]
        self._connection = Connection(
        self._connection: Optional[Connection] = None
        self._events: Deque[Event] = deque()
        self._h11_connection.receive_data(data or b"")
        self._initiating_request = request
        self._initiating_request = Request(
        self._initiating_request: Optional[Request] = None
        self._nonce = generate_nonce()
        self._nonce: Optional[bytes] = None
        self._state = ConnectionState.CONNECTING
        self._state = ConnectionState.OPEN
        self._state = ConnectionState.REJECTING
        self.client = connection_type is ConnectionType.CLIENT
        self.receive_data(h11_client.send(upgrade_request))
        state.
        subprotocol = None
        subprotocols: List[str] = []
        this data can be retrieved with :meth:`events`.
        This should be used if the request has already be received and
        This will either return the connection or raise a
        This will return the bytes to send based on the event or raise
        upgrade = b""
        upgrade = h11.Request(
        upgrade_request = h11.Request(method=b"GET", target=path, headers=headers)
        version = None
        while self._events:
        while True:
    """
    """A Handshake implementation for HTTP/1.1 connections."""
    """Agree on the extensions to use returning an appropriate header value.
    # Client mode methods
    # Server mode methods
    # supported.
    # This raises RemoteProtocolError is the accepted extension is not
    ) -> AcceptConnection:  # noqa: MC0001
    ) -> None:
    ) -> Request:
    @property
    accepted: Iterable[str], supported: Sequence[Extension]
    accepts: Dict[str, Union[bool, bytes]] = {}
    cast,
    def __init__(self, connection_type: ConnectionType) -> None:
    def __repr__(self) -> str:
    def _accept(self, event: AcceptConnection) -> bytes:
    def _establish_client_connection(
    def _initiate_connection(self, request: Request) -> bytes:
    def _process_connection_request(  # noqa: MC0001
    def _reject(self, event: RejectConnection) -> bytes:
    def _send_reject_data(self, event: RejectData) -> bytes:
    def connection(self) -> Optional[Connection]:
    def events(self) -> Generator[Event, None, None]:
    def initiate_upgrade_connection(
    def receive_data(self, data: Optional[bytes]) -> None:
    def send(self, event: Event) -> bytes:
    def state(self) -> ConnectionState:
    Deque,
    Dict,
    extensions = []
    for accept in accepted:
    for offer in requested:
    generate_accept_token,
    generate_nonce,
    Generator,
    if accepts:
    Iterable,
    List,
    LocalProtocolError,
    normed_header_dict,
    Optional,
    RemoteProtocolError,
    requested: Iterable[str], supported: List[Extension]
    return extensions
    return None
    Sequence,
    split_comma_header,
    This returns None if there are no agreed extensions
    Union,
"""
# RFC6455, Section 4.2.1/6 - Reading the Client's Opening Handshake
)
) -> List[Extension]:
) -> Optional[bytes]:
~~~~~~~~~~~~~~~~~~
An implementation of WebSocket handshakes.
class H11Handshake:
def client_extensions_handshake(
def server_extensions_handshake(
from .connection import Connection, ConnectionState, ConnectionType
from .events import AcceptConnection, Event, RejectConnection, RejectData, Request
from .extensions import Extension
from .typing import Headers
from .utilities import (
from collections import deque
from typing import (
import h11
WEBSOCKET_VERSION = b"13"
wsproto/handshake

pass
