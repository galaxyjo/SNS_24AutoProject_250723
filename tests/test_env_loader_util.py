import os
import pytest
from modules.common import env_loader_util


def test_get_env_with_existing_key(monkeypatch):
    monkeypatch.setenv("EXISTING_KEY", "123")
    assert env_loader_util.get_env("EXISTING_KEY") == "123"


def test_get_env_with_missing_key_and_default():
    assert env_loader_util.get_env("MISSING_KEY", default="fallback") == "fallback"


def test_get_env_with_missing_key_and_no_default():
    assert env_loader_util.get_env("MISSING_KEY") is None


def test_require_env_with_existing_key(monkeypatch):
    monkeypatch.setenv("REQUIRED_KEY", "abc")
    assert env_loader_util.require_env("REQUIRED_KEY") == "abc"


def test_require_env_raises(monkeypatch):
    monkeypatch.delenv("REQUIRED_KEY", raising=False)
    with pytest.raises(EnvironmentError):
        env_loader_util.require_env("REQUIRED_KEY")
