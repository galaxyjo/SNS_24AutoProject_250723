
    # if it isn't ignored
    # n.b. mypy complains about the overriding of classes below
    # override connection classes to use emscripten specific classes
    # type: ignore[misc,assignment]
    HTTPConnectionPool.ConnectionCls = EmscriptenHTTPConnection
    HTTPSConnectionPool.ConnectionCls = EmscriptenHTTPSConnection
    urllib3.connection.HTTPConnection = EmscriptenHTTPConnection
    urllib3.connection.HTTPSConnection = EmscriptenHTTPSConnection
def inject_into_urllib3() -> None:
from ...connectionpool import HTTPConnectionPool, HTTPSConnectionPool
from .connection import EmscriptenHTTPConnection, EmscriptenHTTPSConnection
from __future__ import annotations
import urllib3.connection
