# tests/test_network_core.py
# ✅ pytest 기반 테스트

import pytest
from modules.common.network_core import NetworkManager, EmulationManager


def test_network_manager():
    net = NetworkManager()
    net.add_request("req1", {"url": "http://test", "status": 200})
    assert net.get_request("req1")["status"] == 200
    net.clear_requests()
    assert net.get_request("req1") is None


def test_emulation_manager():
    emu = EmulationManager()
    emu.set_emulation("lang", "ko-KR")
    assert emu.get_emulation("lang") == "ko-KR"
    emu.clear_emulation()
    assert emu.get_emulation("lang") is None
