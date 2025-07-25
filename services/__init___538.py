
        "https://github.com/urllib3/urllib3/issues/2680",
        "in a future release of urllib3 2.x. Read more in this issue: "
        "'urllib3[secure]' extra is deprecated and will be removed "
        category=DeprecationWarning,
        stacklevel=2,
    """
    "add_stderr_logger",
    "connection_from_url",
    "disable_warnings",
    "encode_multipart_formdata",
    "get_host",
    "HTTPConnectionPool",
    "HTTPResponse",
    "HTTPSConnectionPool",
    "make_headers",
    "PoolManager",
    "proxy_from_url",
    "ProxyManager",
    "Retry",
    "Timeout",
    # even if urllib3 is vendored within another package.
    # This method needs to be in this __init__.py to get the __name__ correct
    )
    debugging.
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    Helper for quickly adding a StreamHandler to the logger. Useful for
    Helper for quickly disabling all urllib3 warnings.
    import urllib3_secure_extra  # type: ignore # noqa: F401
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.debug("Added a stderr logging handler to logger: %s", __name__)
    logger.setLevel(level)
    pass
    return handler
    Returns the handler after adding it.
    warnings.simplefilter("ignore", category)
    warnings.warn(
"""
# ... Clean up.
# === NOTE TO REPACKAGERS AND VENDORS ===
# All warning filters *must* be appended unless you're really certain that they
# for urllib3 being distributed via PyPI.
# InsecurePlatformWarning's don't vary between requests, so we keep it default.
# mechanisms to silence them.
# Please delete this block, this logic is only
# SecurityWarning's always go off by default.
# See: https://github.com/urllib3/urllib3/issues/2680
# Set default logging handler to avoid "No handler found" warnings.
# shouldn't be: otherwise, it's very hard for users to use most Python
# SNIMissingWarnings should go off only once.
# SubjectAltNameWarning's should go off once per host
)
__all__ = (
__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"
__version__ = __version__
def add_stderr_logger(level=logging.DEBUG):
def disable_warnings(category=exceptions.HTTPWarning):
del NullHandler
else:
except ImportError:
from . import exceptions
from ._version import __version__
from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool, connection_from_url
from .filepost import encode_multipart_formdata
from .poolmanager import PoolManager, ProxyManager, proxy_from_url
from .response import HTTPResponse
from .util.request import make_headers
from .util.retry import Retry
from .util.timeout import Timeout
from .util.url import get_host
from logging import NullHandler
import logging
import warnings
logging.getLogger(__name__).addHandler(NullHandler())
Python HTTP library with thread-safe connection pooling, file post support, user friendly, and more
try:
warnings.simplefilter("always", exceptions.SecurityWarning, append=True)
warnings.simplefilter("default", exceptions.InsecurePlatformWarning, append=True)
warnings.simplefilter("default", exceptions.SNIMissingWarning, append=True)
warnings.simplefilter("default", exceptions.SubjectAltNameWarning, append=True)
