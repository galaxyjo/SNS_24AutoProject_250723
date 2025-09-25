# modules/common/net_socket_engine.py
import socket


class NetSocketEngine:
    def __init__(self, host: str = "localhost", port: int = 8080):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        """Establish a TCP connection to the configured host and port."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, data: bytes):
        """Send bytes over the connected socket."""
        if not self.sock:
            raise ConnectionError("Not connected")
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("data must be bytes or bytearray")
        self.sock.sendall(data)

    def receive(self, bufsize: int = 4096) -> bytes:
        """Receive bytes from the socket."""
        if not self.sock:
            raise ConnectionError("Not connected")
        return self.sock.recv(bufsize)

    def close(self):
        """Close the socket connection."""
        if self.sock:
            self.sock.close()
            self.sock = None
