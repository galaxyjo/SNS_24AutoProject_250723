
            data += self.connection.send(event)
            data += self.handshake.send(event)
            return self.handshake.state
            self.connection = self.handshake.connection
            self.connection.receive_data(data)
            self.handshake.receive_data(data)
            whether the library behaves as a client or as a server.
            yield from self.connection.events()
        """
        :class:`wsproto.events.Event`.
        :param bytes data: Data received from remote peer
        :param wsproto.connection.ConnectionType connection_type: Controls
        :param wsproto.events.Event event: The event to generate data for
        :returns bytes: The data to send to the peer
        :returns: Connection state
        :rtype: wsproto.connection.ConnectionState
        A generator that yields pending events.
        After calling this method, you should call :meth:`events` to see if the
        an event and pass it to this method. This method will return the bytes
        Constructor
        data = b""
        Each event is an instance of a subclass of
        else:
        Feed network data into the connection instance.
        Generate network data for the specified event.
        if self.connection is None:
        if self.connection is not None:
        received data triggered any new events.
        return data
        return self.connection.state
        self, headers: Headers, path: Union[bytes, str]
        self.client = connection_type is ConnectionType.CLIENT
        self.connection: Optional[Connection] = None
        self.handshake = H11Handshake(connection_type)
        self.handshake.initiate_upgrade_connection(headers, path)
        that you should send to the peer.
        When you want to communicate with a WebSocket peer, you should construct
        yield from self.handshake.events()
    """
    ) -> None:
    @property
    def __init__(self, connection_type: ConnectionType) -> None:
    def events(self) -> Generator[Event, None, None]:
    def initiate_upgrade_connection(
    def receive_data(self, data: Optional[bytes]) -> None:
    def send(self, event: Event) -> bytes:
    def state(self) -> ConnectionState:
    Represents the local end of a WebSocket connection to a remote peer.
"""
__all__ = ("ConnectionType", "WSConnection")
__version__ = "1.2.0"
~~~~~~~
A WebSocket implementation.
class WSConnection:
from .connection import Connection, ConnectionState, ConnectionType
from .events import Event
from .handshake import H11Handshake
from .typing import Headers
from typing import Generator, Optional, Union
wsproto
