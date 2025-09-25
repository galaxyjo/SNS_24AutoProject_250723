# modules/common/feature_base.py
class Feature:
    def __init__(self, name, pattern, version):
        self.name = name
        self.pattern = pattern
        self.version = version

    def message_text(self):
        return f"{self.name} is only supported in Python {self.version} and above."


class Features:
    def __init__(self):
        self.mapping = {}

    def add(self, feature: Feature):
        self.mapping[feature.name] = feature

    def __getitem__(self, key):
        return self.mapping[key]

    @property
    def PATTERN(self):
        return " | ".join(f.pattern for f in self.mapping.values())


features = Features()
features.add(Feature("py3k_feature", "power< 'py3k' any* >", "2.7"))

# modules/common/frame_protocol.py
import os
import struct
from codecs import IncrementalDecoder, getincrementaldecoder
from typing import Optional, List, Tuple, Union, Generator


class ParseFailed(Exception):
    pass


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
    def __init__(self, opcode: int, payload: Union[bytes, str], finished: bool, fin: bool):
        self.opcode = opcode
        self.payload = payload
        self.frame_finished = finished
        self.message_finished = fin


class FrameProtocol:
    def __init__(self, client: bool, extensions: Optional[List] = None):
        self.client = client
        self.extensions = extensions or []
        self.buffer = bytearray()

    def feed(self, data: bytes):
        self.buffer.extend(data)

    def process(self):
        if not self.buffer:
            return None
        payload = bytes(self.buffer)
        self.buffer.clear()
        return Frame(Opcode.TEXT, payload.decode("utf-8", errors="ignore"), True, True)

# modules/common/handshake.py
from typing import List, Optional


class HandshakeError(Exception):
    pass


class Handshake:
    def __init__(self, client: bool):
        self.client = client
        self.accepted_protocol: Optional[str] = None

    def initiate(self, protocols: List[str]) -> str:
        if not protocols:
            raise HandshakeError("No protocols provided")
        self.accepted_protocol = protocols[0]
        return self.accepted_protocol

# modules/common/net_socket_engine.py
import socket


class NetSocketEngine:
    def __init__(self, host: str = "localhost", port: int = 8080):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, data: bytes):
        if not self.sock:
            raise ConnectionError("Not connected")
        self.sock.sendall(data)

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None

# modules/common/proxy_accf0cdb.py
class ProxyConfig:
    def __init__(self, proxy_url: str, use_forwarding_for_https: bool = True):
        self.proxy_url = proxy_url
        self.use_forwarding_for_https = use_forwarding_for_https


def connection_requires_http_tunnel(proxy_config: ProxyConfig, destination_scheme: str) -> bool:
    if proxy_config is None or proxy_config.proxy_url is None:
        return False
    if destination_scheme == "http":
        return False
    return True

# modules/common/safe_ssl.py
import ssl
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


class SSLAdapter(HTTPAdapter):
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version or ssl.PROTOCOL_TLSv1_2
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=self.ssl_version,
            **pool_kwargs,
        )

# modules/common/std.py
import queue


class Comparable:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


class tqdm:
    def __init__(self, iterable=None, total=None, desc=None):
        self.iterable = iterable
        self.total = total or (len(iterable) if iterable is not None else 0)
        self.desc = desc
        self.count = 0

    def __iter__(self):
        for item in self.iterable:
            self.count += 1
            self.display()
            yield item

    def display(self):
        print(f"{self.desc or ''} [{self.count}/{self.total}]")


if not hasattr(queue, "SimpleQueue"):
    queue.SimpleQueue = queue.Queue
