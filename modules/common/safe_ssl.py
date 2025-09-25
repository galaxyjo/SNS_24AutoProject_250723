# modules/common/safe_ssl.py
import ssl
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import poolmanager


class SSLAdapter(HTTPAdapter):
    """An HTTPS Transport Adapter that uses an arbitrary SSL version."""

    __attrs__ = HTTPAdapter.__attrs__ + ["ssl_version"]

    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version or ssl.PROTOCOL_TLSv1_2
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        self.poolmanager = poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=self.ssl_version,
            **pool_kwargs,
        )

    def proxy_manager_for(self, *args, **kwargs):
        kwargs["ssl_version"] = self.ssl_version
        return super().proxy_manager_for(*args, **kwargs)
