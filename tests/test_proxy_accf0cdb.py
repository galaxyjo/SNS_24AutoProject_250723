# tests/test_proxy_accf0cdb.py
import pytest
from modules.common.proxy_accf0cdb import ProxyConfig, connection_requires_http_tunnel


def test_tunnel_required_https():
    cfg = ProxyConfig("http://proxy")
    assert connection_requires_http_tunnel(cfg, "https")


def test_no_tunnel_for_http():
    cfg = ProxyConfig("http://proxy")
    assert not connection_requires_http_tunnel(cfg, "http")


def test_no_proxy_config():
    assert not connection_requires_http_tunnel(None, "https")  # type: ignore


def test_proxy_url_none():
    cfg = ProxyConfig(None)  # type: ignore
    assert not connection_requires_http_tunnel(cfg, "https")
