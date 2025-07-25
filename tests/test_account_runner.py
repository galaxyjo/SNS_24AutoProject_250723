
            account    TEXT,
            message    TEXT
            session_id TEXT,
            status     TEXT,
        """
        ("SID1", "acc1", "success", "ok"),
        ("SID2", "acc2", "fail",    "err"),
        )
        CREATE TABLE IF NOT EXISTS account_logs (
    "sid, acc, stat, msg",
    )
    [
    ],
    assert log_account_run(sid, acc, stat, msg) is None
    assert result is None
    conn = sqlite3.connect(account_runner.DB_PATH)
    conn.close()
    conn.commit()
    conn.execute(
    monkeypatch.setattr(account_runner, "ACCOUNTS", ["acc1", "acc2"])
    monkeypatch.setattr(account_runner, "DB_PATH", ":memory:")
    result = asyncio.run(run_all_accounts("SID123"))
# ────────────────────────── 공통 FIXTURE: DB를 메모리로 ──────────────────────────
# ───────────────────────────── run_all_accounts 테스트 ────────────────────────────
# ────────────────────────────── log_account_run 테스트 ─────────────────────────────
# ✅ modules 폴더를 import 경로에 추가
# tests/test_account_runner.py
)
@pytest.fixture(autouse=True)
@pytest.mark.parametrize(
def _in_memory_db(monkeypatch):
def test_log_account_run(sid, acc, stat, msg):
def test_run_all_accounts(monkeypatch):
from modules import account_runner
from modules.account_runner import log_account_run, run_all_accounts
import asyncio
import os
import pytest
import sqlite3
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
