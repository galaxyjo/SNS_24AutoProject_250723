
                "truststore requires peer certificate chain APIs to be available"
                _sslobj = _sslobj._sslobj  # type: ignore[attr-defined]
            ) from None
            _sslmem,
            raise ImportError(
            while not hasattr(_sslobj, "get_unverified_chain"):
        )
        _sslmem = _ssl.MemoryBIO()
        _sslobj = _ssl.create_default_context().wrap_bio(
        del _ssl, _sslobj, _sslmem  # noqa: F821
        except AttributeError:
        import ssl as _ssl
        raise ImportError("truststore requires the 'ssl' module")
        try:
    else:
    except ImportError:
    raise ImportError("truststore requires Python 3.10 or later")
    try:
"""Verify certificates using native system trust stores"""
# Detect Python runtimes which don't implement SSLObject.get_unverified_chain() API
# This API only became public in Python 3.13 but was available in CPython and PyPy since 3.10.
__all__ = ["SSLContext", "inject_into_ssl", "extract_from_ssl"]
__version__ = "0.10.0"
del _api, _sys  # type: ignore[name-defined] # noqa: F821
from ._api import SSLContext, extract_from_ssl, inject_into_ssl  # noqa: E402
if _sys.version_info < (3, 10):
if _sys.version_info < (3, 13):
import sys as _sys
