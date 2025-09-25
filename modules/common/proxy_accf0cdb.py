# modules/common/proxy_accf0cdb.py
class ProxyConfig:
    def __init__(self, proxy_url: str, use_forwarding_for_https: bool = True):
        self.proxy_url = proxy_url
        self.use_forwarding_for_https = use_forwarding_for_https


def connection_requires_http_tunnel(proxy_config: "ProxyConfig", destination_scheme: str) -> bool:
    """Return True if the connection requires an HTTP CONNECT tunnel."""
    if proxy_config is None or proxy_config.proxy_url is None:
        return False
    if destination_scheme == "http":
        return False
    return True
