# tests/test_safe_ssl.py
import ssl
import pytest
from modules.common.safe_ssl import SSLAdapter


def test_ssl_adapter_init_default():
    adapter = SSLAdapter()
    assert adapter.ssl_version == ssl.PROTOCOL_TLSv1_2


def test_ssl_adapter_custom_version():
    adapter = SSLAdapter(ssl_version=ssl.PROTOCOL_TLS_CLIENT)
    assert adapter.ssl_version == ssl.PROTOCOL_TLS_CLIENT


def test_ssl_adapter_init_poolmanager(monkeypatch):
    adapter = SSLAdapter()

    called = {}
    def dummy_poolmanager(**kwargs):
        called.update(kwargs)
        return "pool"

    monkeypatch.setattr("modules.common.safe_ssl.poolmanager.PoolManager", dummy_poolmanager)
    adapter.init_poolmanager(connections=5, maxsize=10, block=True)
    assert called["ssl_version"] == adapter.ssl_version


def test_ssl_adapter_proxy_manager_for(monkeypatch):
    adapter = SSLAdapter()
    def dummy_proxy_manager_for(*args, **kwargs):
        return kwargs
    monkeypatch.setattr("requests.adapters.HTTPAdapter.proxy_manager_for", dummy_proxy_manager_for)
    result = adapter.proxy_manager_for("http://proxy")
    assert result["ssl_version"] == adapter.ssl_version
