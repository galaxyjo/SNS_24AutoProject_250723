
            block=block,
            kwargs["ssl_version"] = self.ssl_version
            maxsize=maxsize,
            num_pools=connections,
            return super().proxy_manager_for(*args, **kwargs)
            ssl_version=self.ssl_version,
        # conditionally define this method.
        # don't allow passing arbitrary keyword arguments. As a result, only
        # Earlier versions of requests either don't have this method or, worse,
        )
        >>> from requests_toolbelt import SSLAdapter
        >>> import requests
        >>> import ssl
        >>> s = requests.Session()
        >>> s.mount('https://', SSLAdapter(ssl.PROTOCOL_TLSv1))
        def proxy_manager_for(self, *args, **kwargs):
        self.poolmanager = poolmanager.PoolManager(
        self.ssl_version = ssl_version
        super().__init__(**kwargs)
    """
    __attrs__ = HTTPAdapter.__attrs__ + ["ssl_version"]
    A HTTPS Adapter for Python Requests that allows the choice of the SSL/TLS
    choice of high-security TLS versions (where supported), or to work around
    code. In earlier versions of Requests, this adapter will not function
    def __init__(self, *args, **kwargs): pass
    def __init__(self, ssl_version=None, **kwargs):
    def init_poolmanager(self, connections, maxsize, block=False):
    default Python SSL module. All subsequent requests that match the adapter
    Example usage:
    if requests.__build__ >= 0x020400:
    misbehaving servers that fail to correctly negotiate the default TLS
    prefix will use the chosen SSL version instead of the default.
    prior to Requests v2.4.0 the adapter did not have access to the proxy setup
    properly when used with proxies.
    Requests when using a proxy. However, this may not always be possible:
    This adapter will also attempt to change the SSL/TLS version negotiated by
    version being offered.
    version negotiated by Requests. This can be used either to enforce the
    You can replace the chosen protocol with any that are available in the
"""
# -*- coding: utf-8 -*-
=============================
class SSLAdapter:
from .._compat import poolmanager
from requests.adapters import HTTPAdapter
https://lukasa.co.uk/2013/01/Choosing_SSL_Version_In_Requests/
import requests
in this blog post:
requests_toolbelt.ssl_adapter
This file contains an implementation of the SSLAdapter originally demonstrated
