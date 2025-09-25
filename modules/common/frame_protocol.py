# modules/common/frame_protocol.py
import struct
from typing import Optional, List, Union


class ParseFailed(Exception):
    """Raised when a WebSocket frame cannot be parsed correctly."""


class CloseReason:
    NORMAL_CLOSURE = 1000
    PROTOCOL_ERROR = 1002
    UNSUPPORTED_DATA = 1003
    NO_STATUS_RCVD = 1005
    ABNORMAL_CLOSURE = 1006
    INVALID_FRAME_PAYLOAD_DATA = 1007
    POLICY_VIOLATION = 1008
    MESSAGE_TOO_BIG = 1009
    MANDATORY_EXT = 1010
    INTERNAL_ERROR = 1011
    SERVICE_RESTART = 1012
    TRY_AGAIN_LATER = 1013
    TLS_HANDSHAKE_FAILED = 1015


class Opcode:
    CONTINUATION = 0x0
    TEXT = 0x1
    BINARY = 0x2
    CLOSE = 0x8
    PING = 0x9
    PONG = 0xA


class Frame:
    def __init__(self, opcode: int, payload: Union[bytes, str], frame_finished: bool, message_finished: bool):
        self.opcode = opcode
        self.payload = payload
        self.frame_finished = frame_finished
        self.message_finished = message_finished


class FrameProtocol:
    """
    Simplified WebSocket frame protocol handler.
    """

    def __init__(self, client: bool, extensions: Optional[List] = None):
        self.client = client
        self.extensions = extensions or []
        self.buffer = bytearray()

    def feed(self, data: bytes):
        """Feed raw data into the buffer for processing."""
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("data must be bytes or bytearray")
        self.buffer.extend(data)

    def process(self) -> Optional[Frame]:
        """Process buffered data and return a Frame if possible."""
        if not self.buffer:
            return None

        payload = bytes(self.buffer)
        self.buffer.clear()

        try:
            # For simplicity, decode as UTF-8 text
            decoded = payload.decode("utf-8", errors="ignore")
            return Frame(Opcode.TEXT, decoded, True, True)
        except Exception as e:
            raise ParseFailed(f"Failed to parse frame: {e}")


# Notes:
# Payload length used 2 bytes when 1 would have sufficed  (RFC6455 guidance)
# This simplified implementation does not strictly enforce all WebSocket specs.
