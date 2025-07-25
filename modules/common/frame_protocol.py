
                    "Error decoding CLOSE reason: " + str(exc),
                    "Payload length used 2 bytes when 1 would have sufficed"
                    "Payload length used 8 bytes when 2 would have sufficed"
                    closed = True
                    CloseReason.INVALID_FRAME_PAYLOAD_DATA,
                    final += result
                    frame = self._message_decoder.process_frame(frame)
                    frame = self._process_close(frame)
                    raise ParseFailed("error in extension", result)
                    reason.encode("utf-8"), MAX_PAYLOAD_NORMAL - 2
                    rsv_used[bit] = True
                # I'm not sure why this is illegal, but that's what the RFC
                # says, so...
                )
                break
                code = CloseReason(code)
                data = self.decoder.decode(frame.payload, finished)
                elif frame.opcode == Opcode.CLOSE:
                header += bytearray(struct.pack("!H", second_payload))
                header += bytearray(struct.pack("!Q", second_payload))
                if isinstance(result, CloseReason):
                if not frame.opcode.iscontrol():
                if result is not None:
                if used:
                pass
                payload += _truncate_utf8(
                raise ParseFailed(
                raise ParseFailed("8-byte payload length with non-zero MSB")
                raise ParseFailed("CLOSE with invalid code")
                raise ParseFailed("CLOSE with unknown reserved code")
                raise ParseFailed("error in extension", payload_)
                raise ParseFailed("error in extension", result)
                raise ParseFailed("remote CLOSE with local-only reason")
                raise ParseFailed("Reserved bit set unexpectedly")
                raise ParseFailed("unexpected CONTINUATION")
                raise ParseFailed(str(exc), CloseReason.INVALID_FRAME_PAYLOAD_DATA)
                raise ValueError("payload too long for control frame")
                reason = data[2:].decode("utf-8")
                result = extension.frame_inbound_complete(self, self.header.fin)
                return False
                return None
                self._masking_key[key_rotation:] + self._masking_key[:key_rotation]
                self.buffer.rollback()
                yield event
            #   -- https://tools.ietf.org/html/rfc6455#section-5.3
            # "If this Close control frame contains no status code, _The
            # "The masking key is a 32-bit value chosen at random by the
            # appear on the wire."
            # authors of malicious applications from selecting the bytes that
            # client.  When preparing a masked frame, the client MUST pick a
            # fresh masking key from the set of allowed 32-bit values.  The
            # key for a given frame MUST NOT make it simple for a server/proxy
            # masking key needs to be unpredictable; thus, the masking key
            # MUST be derived from a strong source of entropy, and the masking
            # Rotate the masking key so that the next usage continues
            # to predict the masking key for a subsequent frame.  The
            # unpredictability of the masking key is essential to prevent
            # WebSocket Connection Close Code_ is considered to be 1005"
            # with the next key element, rather than restarting.
            (code,) = struct.unpack("!H", data[:2])
            (payload_len,) = struct.unpack("!H", data)
            (payload_len,) = struct.unpack("!Q", data)
            )
            a, b, c, d = (_XOR_TABLE[n] for n in self._masking_key)
            assert isinstance(frame.payload, (bytes, bytearray))
            bool(data[0] & RSV1_MASK),
            bool(data[0] & RSV2_MASK),
            bool(data[0] & RSV3_MASK),
            code = CloseReason.NORMAL_CLOSURE
            code = None
            data = (CloseReason.NO_STATUS_RCVD, "")
            data = (code, reason)
            data = frame.payload
            data = self.buffer.consume_exactly(2)
            data = self.buffer.consume_exactly(8)
            data_array = bytearray(data)
            data_array[::4] = data_array[::4].translate(a)
            data_array[1::4] = data_array[1::4].translate(b)
            data_array[2::4] = data_array[2::4].translate(c)
            data_array[3::4] = data_array[3::4].translate(d)
            else:
            except UnicodeDecodeError as exc:
            except ValueError:
            final = bytearray()
            first_payload |= 1 << 7
            first_payload = payload_length
            first_payload = PAYLOAD_LENGTH_EIGHT_BYTE
            first_payload = PAYLOAD_LENGTH_TWO_BYTE
            for bit, used in enumerate(result):
            for extension in self.extensions:
            frame = self._frame_decoder.process_buffer()
            if code < MIN_CLOSE_REASON or code > MAX_CLOSE_REASON:
            if code in LOCAL_ONLY_CLOSE_REASONS:
            if data is None:
            if event is None:
            if found and not expected:
            if frame is not None:
            if frame.opcode is Opcode.CONTINUATION:
            if isinstance(payload_, CloseReason):
            if isinstance(result, CloseReason):
            if masking_key is None:
            if not isinstance(code, CloseReason) and code <= MAX_PROTOCOL_CLOSE_REASON:
            if not self.parse_header():
            if opcode.iscontrol():
            if payload_len <= MAX_PAYLOAD_NORMAL:
            if payload_len <= MAX_PAYLOAD_TWO_BYTE:
            if payload_len >> 63:
            if quad_payload:
            if reason is not None:
            key_rotation = len(data) % 4
            masker = XorMaskerSimple(masking_key)
            masking_key = os.urandom(4)
            masking_key = self.buffer.consume_exactly(4)
            opcode = Opcode(opcode)
            opcode = Opcode.BINARY
            opcode = Opcode.CONTINUATION
            opcode = Opcode.TEXT
            payload += bytearray(struct.pack("!H", code))
            payload += final
            payload = payload.encode("utf-8")
            payload = payload_
            payload_ = extension.frame_inbound_payload_data(self, payload)
            quad_payload = True
            raise ParseFailed("client received unexpected masked frame")
            raise ParseFailed("CLOSE with 1 byte payload")
            raise ParseFailed("Control frame with payload len > 125")
            raise ParseFailed("expected CONTINUATION, got %r" % frame.opcode)
            raise ParseFailed("Invalid attempt to fragment control frame")
            raise ParseFailed("server received unexpected unmasked frame")
            raise ParseFailed(f"Invalid opcode {opcode:#x}")
            raise TypeError("cannot specify a reason without a code")
            raise TypeError("Data type mismatch inside message")
            raise ValueError("Must provide bytes or text")
            result = extension.frame_inbound_header(self, opcode, rsv, payload_len)
            return bytearray()
            return bytes(data_array)
            return False
            return header + masking_key + masker.process(payload)
            return None
            rsv, payload = extension.frame_outbound(self, opcode, rsv, payload, fin)
            second_payload = None
            second_payload = payload_length
            self._masking_key = (
            self._outbound_opcode = None
            self._outbound_opcode = opcode
            self.buffer.rollback()
            self.decoder = getincrementaldecoder("utf-8")()
            self.decoder = None
            self.effective_opcode = None
            self.effective_opcode = Opcode.CONTINUATION
            self.feed(initial_bytes)
            self.header = None
            self.masker = None
            self.masker = XorMaskerNull()
            self.masker = XorMaskerSimple(masking_key)
            self.opcode = frame.opcode
            self.opcode = None
            self.payload_required = 0
            self.payload_required = payload_len
            try:
            yield frame
        # Consume as much as we can from self._buffer, yielding events, and
        # disabled extensions in the first place...
        # Global state
        # In CPython 3.4+, del[:n] is amortized O(n), *not* quadratic
        # parse_header() sets these.
        # then yield None when we need more data. Or raise ParseFailed.
        # XX FIXME this should probably be refactored so that we never see
        )
        assert isinstance(data, (bytes, bytearray))
        assert not frame.opcode.iscontrol()
        assert self.effective_opcode is not None
        assert self.header is not None
        assert self.masker is not None
        closed = False
        data = frame.payload
        data = self.buffer.consume_exactly(2)
        data = self.buffer[self.bytes_used: self.bytes_used + nbytes]
        del self.buffer[: self.bytes_used]
        elif frame.opcode is not Opcode.CONTINUATION:
        elif isinstance(payload, str):
        elif len(data) == 1:
        elif payload_len == PAYLOAD_LENGTH_EIGHT_BYTE:
        elif payload_length <= MAX_PAYLOAD_TWO_BYTE:
        elif self._outbound_opcode is not opcode:
        else:
        except ValueError:
        fin = bool(data[0] & FIN_MASK)
        fin_bits = int(fin) << 7
        fin_rsv_opcode = self._make_fin_rsv_opcode(fin, rsv, opcode)
        finished = frame.frame_finished and frame.message_finished
        finished = self.payload_consumed == self.header.payload_len
        for event in self._parse_more:
        for expected, found in zip(rsv_used, rsv):
        for extension in reversed(self.extensions):
        for extension in self.extensions:
        frame = Frame(self.effective_opcode, payload, finished, self.header.fin)
        frame = Frame(self.opcode, data, frame.frame_finished, finished)
        has_mask = bool(data[1] & MASK_MASK)
        header = bytearray([fin_rsv_opcode, first_payload])
        if code in LOCAL_ONLY_CLOSE_REASONS:
        if code is CloseReason.NO_STATUS_RCVD:
        if code is None and reason:
        if code is not None:
        if data is None:
        if data:
        if fin:
        if finished:
        if frame.opcode is Opcode.TEXT:
        if has_mask and self.client:
        if has_mask:
        if initial_bytes:
        if isinstance(payload, (bytes, bytearray, memoryview)):
        if len(self.buffer) - self.bytes_used < nbytes:
        if len(self.buffer) < self.payload_required:
        if not data:
        if not has_mask and not self.client:
        if not nbytes:
        if not payload and self.header.payload_len > 0:
        if not self.header:
        if opcode.iscontrol() and not fin:
        if opcode.iscontrol() and payload_len > MAX_PAYLOAD_NORMAL:
        if payload_len == PAYLOAD_LENGTH_TWO_BYTE:
        if payload_len is None:
        if payload_length <= MAX_PAYLOAD_NORMAL:
        if second_payload is not None:
        if self._outbound_opcode is None:
        if self.client:
        if self.decoder is None:
        if self.header.opcode.iscontrol():
        if self.opcode is None:
        opcode = data[0] & OPCODE_MASK
        opcode_bits = int(opcode)
        payload = bytearray()
        payload = self.buffer.consume_at_most(payload_remaining)
        payload = self.masker.process(payload)
        payload_len = self.parse_extended_payload_length(opcode, payload_len_short)
        payload_len_short = data[1] & PAYLOAD_LEN_MASK
        payload_length = len(payload)
        payload_remaining = self.header.payload_len - self.payload_consumed
        quad_payload = False
        return bool(self & 0x08)
        return data
        return fin_bits | rsv_bits | opcode_bits
        return frame
        return Frame(frame.opcode, data, frame.frame_finished, frame.message_finished)
        return header + payload
        return len(self.buffer)
        return payload_len
        return self._serialize_frame(opcode, payload, fin)
        return self._serialize_frame(Opcode.CLOSE, payload)
        return self._serialize_frame(Opcode.PING, payload)
        return self._serialize_frame(Opcode.PONG, payload)
        return self.consume_at_most(nbytes)
        return True
        rsv = RsvBits(
        rsv = RsvBits(False, False, False)
        rsv_bits = (int(rsv.rsv1) << 6) + (int(rsv.rsv2) << 5) + (int(rsv.rsv3) << 4)
        rsv_used = [False, False, False]
        self, client: bool, extensions: Optional[List["Extension"]] = None
        self, msg: str, code: CloseReason = CloseReason.PROTOCOL_ERROR
        self, opcode: Opcode, payload: bytes = b"", fin: bool = True
        self, opcode: Opcode, payload_len: int
        self, opcode: Opcode, rsv: RsvBits, payload_len: int
        self, payload: Union[bytes, bytearray, str] = b"", fin: bool = True
        self._frame_decoder = FrameDecoder(self.client, self.extensions)
        self._frame_decoder.receive_bytes(data)
        self._masking_key = masking_key
        self._message_decoder = MessageDecoder()
        self._outbound_opcode: Optional[Opcode] = None
        self._parse_more = self._parse_more_gen()
        self.buffer += new_bytes
        self.buffer = Buffer()
        self.buffer = bytearray()
        self.buffer.commit()
        self.buffer.feed(data)
        self.bytes_used += len(data)
        self.bytes_used = 0
        self.client = client
        self.code = code
        self.decoder: Optional[IncrementalDecoder] = None
        self.effective_opcode = self.header.opcode
        self.effective_opcode: Optional[Opcode] = None
        self.extension_processing(opcode, rsv, payload_len)
        self.extensions = [ext for ext in extensions if ext.enabled()]
        self.extensions = [ext for ext in self.extensions if ext.enabled()]
        self.extensions = extensions or []
        self.header = Header(fin, rsv, opcode, payload_len, None)
        self.header: Optional[Header] = None
        self.masker: Union[None, XorMaskerNull, XorMaskerSimple] = None
        self.opcode: Optional[Opcode] = None
        self.payload_consumed += len(payload)
        self.payload_consumed = 0
        self.payload_required = 0
        super().__init__(msg)
        try:
        while not closed:
    """
    # But we might have cut a codepoint in half, in which case we want to
    # discard the partial character so the data is at least
    # DON'T DEFINE THIS: RESERVED_1004 = 1004
    # few characters, but since this is only used for close messages (max
    # length = 125 bytes) it really doesn't matter.
    # Truncate
    # well-formed. This is a little inefficient since it processes the
    # whole message twice when in theory we could just peek at the last
    #: (e.g., the server certificate can't be verified).
    #: (not part of RFC6455)
    #: applications expecting a status code to indicate that no status
    #: applications expecting a status code to indicate that the
    #: are needed SHOULD appear in the /reason/ part of the Close frame.
    #: because it has received a message that is too big for it to
    #: because it has received a message that violates its policy.  This
    #: because it has received a type of data it cannot accept (e.g., an
    #: because it has received data within a message that was not
    #: Binary message
    #: can fail the WebSocket handshake instead.
    #: Close control frame by an endpoint.  It is designated for use in
    #: Close frame
    #: code was actually present.
    #: connection because it has expected the server to negotiate one or
    #: connection was closed abnormally, e.g., without sending or
    #: connection was closed due to a failure to perform a TLS handshake
    #: consistent with the type of the message (e.g., non-UTF-8 [RFC3629]
    #: Continuation frame
    #: data within a text message).
    #: endpoint that understands only text data MAY send this if it
    #: fulfilling the request.
    #: going down or a browser having navigated away from a page.
    #: indicates a normal closure, meaning that the purpose for
    #: indicates that a server is terminating the connection because
    #: indicates that an endpoint (client) is terminating the
    #: indicates that an endpoint is "going away", such as a server
    #: indicates that an endpoint is terminating the connection
    #: indicates that an endpoint is terminating the connection due
    #: is a generic status code that can be returned when there is no
    #: is a need to hide specific details about the policy.
    #: is a reserved value and MUST NOT be set as a status code in a
    #: it encountered an unexpected condition that prevented it from
    #: message of the WebSocket handshake.  The list of extensions that
    #: more extension, but the server didn't return them in the response
    #: Note that this status code is not used by the server, because it
    #: other more suitable status code (e.g., 1003 or 1009) or if there
    #: Ping frame
    #: Pong frame
    #: process.
    #: receives a binary message).
    #: receiving a Close control frame.
    #: Reserved.  The specific meaning might be defined in the future.
    #: Server/service is restarting
    #: Temporary server condition forced blocking client's request
    #: Text message
    #: to a protocol error.
    #: which the connection was established has been fulfilled.
    ) -> bytes:
    ) -> None:
    ) -> Optional[int]:
    ABNORMAL_CLOSURE = 1006
    BINARY = 0x2
    CLOSE = 0x8
    CloseReason.ABNORMAL_CLOSURE,
    CloseReason.NO_STATUS_RCVD,
    CloseReason.TLS_HANDSHAKE_FAILED,
    CONTINUATION = 0x0
    data = data.decode("utf-8", errors="ignore").encode("utf-8")
    data = data[:nbytes]
    def __init__(
    def __init__(self) -> None:
    def __init__(self, *args, **kwargs): pass
    def __init__(self, client: bool, extensions: List["Extension"]) -> None:
    def __init__(self, initial_bytes: Optional[bytes] = None) -> None:
    def __init__(self, masking_key: bytes) -> None:
    def __len__(self) -> int:
    def _make_fin_rsv_opcode(self, fin: bool, rsv: RsvBits, opcode: Opcode) -> int:
    def _parse_more_gen(self) -> Generator[Optional[Frame], None, None]:
    def _process_close(self, frame: Frame) -> Frame:
    def _serialize_frame(
    def close(self, code: Optional[int] = None, reason: Optional[str] = None) -> bytes:
    def commit(self) -> None:
    def consume_at_most(self, nbytes: int) -> bytes:
    def consume_exactly(self, nbytes: int) -> Optional[bytes]:
    def extension_processing(
    def feed(self, new_bytes: bytes) -> None:
    def iscontrol(self) -> bool:
    def parse_extended_payload_length(
    def parse_header(self) -> bool:
    def ping(self, payload: bytes = b"") -> bytes:
    def pong(self, payload: bytes = b"") -> bytes:
    def process(self, data: bytes) -> bytes:
    def process_buffer(self) -> Optional[Frame]:
    def process_frame(self, frame: Frame) -> Frame:
    def receive_bytes(self, data: bytes) -> None:
    def received_frames(self) -> Generator[Frame, None, None]:
    def rollback(self) -> None:
    def send_data(
    fin: bool
    frame_finished: bool
    from .extensions import Extension  # pragma: no cover
    GOING_AWAY = 1001
    if len(data) <= nbytes:
    INTERNAL_ERROR = 1011
    INVALID_FRAME_PAYLOAD_DATA = 1007
    MANDATORY_EXT = 1010
    masking_key: Optional[bytes]
    message_finished: bool
    MESSAGE_TOO_BIG = 1009
    NO_STATUS_RCVD = 1005
    NORMAL_CLOSURE = 1000
    opcode: Opcode
    payload: Union[bytes, str, Tuple[int, str]]
    payload_len: int
    PING = 0x9
    POLICY_VIOLATION = 1008
    PONG = 0xA
    PROTOCOL_ERROR = 1002
    return data
    RFC 6455, Section 5.2 - Base Framing Protocol
    RFC 6455, Section 7.4.1 - Defined Status Codes
    rsv: RsvBits
    rsv1: bool
    rsv2: bool
    rsv3: bool
    SERVICE_RESTART = 1012
    TEXT = 0x1
    TLS_HANDSHAKE_FAILED = 1015
    TRY_AGAIN_LATER = 1013
    UNSUPPORTED_DATA = 1003
"""
# FIN, RSV[123] and OPCODE are packed into a single byte
# MASK and PAYLOAD LEN are packed into a byte
# Payload length constants
# RFC 6455, Section 7.4.1 - Defined Status Codes
# RFC 6455, Section 7.4.2 - Status Code Ranges
# RFC6455, Section 5.2 - Base Framing Protocol
)
_XOR_TABLE = [bytes(a ^ b for a in range(256)) for b in range(256)]
~~~~~~~~~~~~~~~~~~~~~~
class Buffer:
class CloseReason:
class Frame:
class FrameDecoder:
class FrameProtocol:
class Header:
class MessageDecoder:
class Opcode:
class ParseFailed:
class RsvBits:
class XorMaskerNull:
class XorMaskerSimple:
def _truncate_utf8(data: bytes, nbytes: int) -> bytes:
FIN_MASK = 0x80
from codecs import getincrementaldecoder, IncrementalDecoder
from typing import Generator, List, Optional, Tuple, TYPE_CHECKING, Union
if TYPE_CHECKING:
import os
import struct
LOCAL_ONLY_CLOSE_REASONS = (
MASK_MASK = 0x80
MAX_CLOSE_REASON = 4999
MAX_FRAME_PAYLOAD = MAX_PAYLOAD_EIGHT_BYTE
MAX_LIBRARY_CLOSE_REASON = 3999
MAX_PAYLOAD_EIGHT_BYTE = 2**64 - 1
MAX_PAYLOAD_NORMAL = 125
MAX_PAYLOAD_TWO_BYTE = 2**16 - 1
MAX_PRIVATE_CLOSE_REASON = 4999
MAX_PROTOCOL_CLOSE_REASON = 2999
MIN_CLOSE_REASON = 1000
MIN_LIBRARY_CLOSE_REASON = 3000
MIN_PRIVATE_CLOSE_REASON = 4000
MIN_PROTOCOL_CLOSE_REASON = 1000
NULL_MASK = struct.pack("!I", 0)
OPCODE_MASK = 0x0F
PAYLOAD_LEN_MASK = 0x7F
PAYLOAD_LENGTH_EIGHT_BYTE = 127
PAYLOAD_LENGTH_TWO_BYTE = 126
RSV1_MASK = 0x40
RSV2_MASK = 0x20
RSV3_MASK = 0x10
WebSocket frame protocol implementation.
wsproto/frame_protocol
