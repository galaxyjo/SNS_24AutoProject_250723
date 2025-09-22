
and proxy_config
        and proxy_config.use_forwarding_for_https
        Proxy configuration from poolmanager.py
        proxy_url.scheme == "https"
        return False
        The scheme of the destination. (i.e https, http, etc)
        URL of the proxy.
    """
    # HTTP destinations never require tunneling, we always forward.
    # If we're not using a proxy, no way to use a tunnel.
    # Otherwise always use a tunnel.
    # Support for forwarding with HTTPS proxies and HTTPS destinations.
    ):
    :param ProxyConfig proxy_config:
    :param str destination_scheme:
    :param URL proxy_url:
    destination_scheme: str | None = None,
    from ..connection import ProxyConfig
    if (
    if destination_scheme == "http":
    if proxy_url is None:
    proxy_config: ProxyConfig | None = None,
    proxy_url: Url | None = None,
    return True
    Returns True if the connection requires an HTTP CONNECT through the proxy.
# -*- coding: utf-8 -*-
) -> bool:
def connection_requires_http_tunnel(
from .url import Url
from __future__ import annotations
if typing.TYPE_CHECKING:
import typing

pass
