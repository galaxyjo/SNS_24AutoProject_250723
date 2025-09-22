import sys
import pytest
from modules.common import sys_util


def test_is_windows(monkeypatch):
    monkeypatch.setattr(sys, "platform", "win32")
    assert sys_util.is_windows() is True
    assert sys_util.is_linux() is False
    assert sys_util.is_mac() is False


def test_is_linux(monkeypatch):
    monkeypatch.setattr(sys, "platform", "linux")
    assert sys_util.is_windows() is False
    assert sys_util.is_linux() is True
    assert sys_util.is_mac() is False


def test_is_mac(monkeypatch):
    monkeypatch.setattr(sys, "platform", "darwin")
    assert sys_util.is_windows() is False
    assert sys_util.is_linux() is False
    assert sys_util.is_mac() is True
