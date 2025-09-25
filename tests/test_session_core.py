# tests/test_session_core.py
# ============================================
# 📌 테스트 파일: test_session_core.py
# 📂 대상: modules/common/session_core.py
# ============================================

import pytest
from modules.common.session_core import Session


class DummyConn:
    """테스트용 더미 연결"""
    def __init__(self):
        self.last_cmd = None

    def execute(self, cmd):
        self.last_cmd = cmd
        return {"ok": True, "cmd": cmd}


def test_status_command():
    conn = DummyConn()
    s = Session(conn)
    result = s.status()
    assert result["ok"] is True
    assert "session.status" in result["cmd"]["method"]


def test_subscribe_unsubscribe():
    conn = DummyConn()
    s = Session(conn)

    result_sub = s.subscribe("log.entryAdded", browsing_contexts=["ctx1"])
    assert result_sub["ok"] is True
    assert "session.subscribe" in result_sub["cmd"]["method"]

    result_unsub = s.unsubscribe("log.entryAdded")
    assert result_unsub["ok"] is True
    assert "session.unsubscribe" in result_unsub["cmd"]["method"]
