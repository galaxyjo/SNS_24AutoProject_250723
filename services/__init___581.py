
            "See: https://github.com/urllib3/urllib3/issues/2168"
            "See: https://github.com/urllib3/urllib3/issues/3020",
            "urllib3 v2 only supports OpenSSL 1.1.1+, currently "
            exceptions.NotOpenSSLWarning,
            f"the 'ssl' module is compiled with {ssl.OPENSSL_VERSION!r}. "
        )
        :class:`~urllib3.exceptions.MaxRetryError` exception.
        :class:`~urllib3.util.retry.Retry` object for fine-grained control
        :class:`urllib3.util.Timeout`.
        303, 307, 308). Each redirect counts as a retry. Disabling retries
        an iterable of :class:`str`/:class:`bytes`, or a file-like object.
        body=body,
        but no other types of errors. Pass zero to never retry.
        Configure the number of retries to allow before raising a
        'content-encoding' header.
        Data to encode and send as JSON with UTF-encoded in the request body.
        Data to encode and send in the request body.
        Data to send in the request body, either :class:`str`, :class:`bytes`,
        decode_content=decode_content,
        Dictionary of custom headers to send, such as User-Agent,
        fields=fields,
        headers=headers,
        HTTP request method (such as GET, POST, PUT, etc.)
        If ``False``, then retries are disabled and any exception is raised
        If ``None`` (default) will retry 3 times, see ``Retry.DEFAULT``. Pass a
        If specified, overrides the default timeout for this one
        If True, automatically handle redirects (status codes 301, 302,
        If True, the response's body will be preloaded into memory.
        If True, will attempt to decode the body based on the
        If-None-Match, etc.
        immediately. Also, instead of raising a MaxRetryError on redirects,
        json=json,
        method,
        over different types of retries.
        Pass an integer number to retry connection errors that many times,
        preload_content=preload_content,
        raise ImportError(
        redirect=redirect,
        request. It may be a float (in seconds) or an instance of
        retries=retries,
        The ``"Content-Type"`` header will be set to ``"application/json"``
        the redirect response will be returned.
        The URL to perform the request on.
        timeout=timeout,
        unless specified otherwise.
        url,
        warnings.warn(
        will disable redirect, too.
    """
    "add_stderr_logger",
    "BaseHTTPResponse",
    "connection_from_url",
    "disable_warnings",
    "encode_multipart_formdata",
    "HTTPConnectionPool",
    "HTTPHeaderDict",
    "HTTPResponse",
    "HTTPSConnectionPool",
    "make_headers",
    "PoolManager",
    "proxy_from_url",
    "ProxyManager",
    "request",
    "Retry",
    "Timeout",
    # even if urllib3 is vendored within another package.
    # This method needs to be in this __init__.py to get the __name__ correct
    )
    *,
    :param body:
    :param bool decode_content:
    :param bool preload_content:
    :param fields:
    :param headers:
    :param json:
    :param method:
    :param redirect:
    :param retries:
    :param timeout:
    :param url:
    :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.
    A convenience, top-level request method. It uses a module-global ``PoolManager`` instance.
    body: _TYPE_BODY | None = None,
    debugging.
    decode_content: bool | None = True,
    elif ssl.OPENSSL_VERSION_INFO < (1, 1, 1):  # Defensive:
    fields: _TYPE_FIELDS | None = None,
    from .contrib.emscripten import inject_into_urllib3  # noqa: 401
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    headers: typing.Mapping[str, str] | None = None,
    Helper for quickly adding a StreamHandler to the logger. Useful for
    Helper for quickly disabling all urllib3 warnings.
    if not ssl.OPENSSL_VERSION.startswith("OpenSSL "):  # Defensive:
    import ssl
    inject_into_urllib3()
    json: typing.Any | None = None,
    level: int = logging.DEBUG,
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.debug("Added a stderr logging handler to logger: %s", __name__)
    logger.setLevel(level)
    method: str,
    pass
    preload_content: bool | None = True,
    redirect: bool | None = True,
    retries: Retry | bool | int | None = None,
    return _DEFAULT_POOL.request(
    return handler
    Returns the handler after adding it.
    The method does not accept low-level ``**urlopen_kw`` keyword arguments.
    Therefore, its side effects could be shared across dependencies relying on it.
    timeout: Timeout | float | int | None = 3,
    To avoid side effects create a new ``PoolManager`` instance and use it instead.
    url: str,
    warnings.simplefilter("ignore", category)
"""
# ... Clean up.
# All warning filters *must* be appended unless you're really certain that they
# Ensure that Python is compiled with OpenSSL 1.1.1+
# fine, we only care if the module is available.
# If the 'ssl' module isn't available at all that's
# InsecurePlatformWarning's don't vary between requests, so we keep it default.
# mechanisms to silence them.
# SecurityWarning's always go off by default.
# Set default logging handler to avoid "No handler found" warnings.
# shouldn't be: otherwise, it's very hard for users to use most Python
)
) -> BaseHTTPResponse:
) -> logging.StreamHandler[typing.TextIO]:
__all__ = (
__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"
__version__ = __version__
_DEFAULT_POOL = PoolManager()
def add_stderr_logger(
def disable_warnings(category: type[Warning] = exceptions.HTTPWarning) -> None:
def request(
del NullHandler
else:
except ImportError:
from . import exceptions
from ._base_connection import _TYPE_BODY
from ._collections import HTTPHeaderDict
from ._version import __version__
from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool, connection_from_url
from .filepost import _TYPE_FIELDS, encode_multipart_formdata
from .poolmanager import PoolManager, ProxyManager, proxy_from_url
from .response import BaseHTTPResponse, HTTPResponse
from .util.request import make_headers
from .util.retry import Retry
from .util.timeout import Timeout
from __future__ import annotations
from logging import NullHandler
if sys.platform == "emscripten":
import logging
import sys
import typing
import warnings
logging.getLogger(__name__).addHandler(NullHandler())
Python HTTP library with thread-safe connection pooling, file post support, user friendly, and more
try:
warnings.simplefilter("always", exceptions.SecurityWarning, append=True)
warnings.simplefilter("default", exceptions.InsecurePlatformWarning, append=True)
