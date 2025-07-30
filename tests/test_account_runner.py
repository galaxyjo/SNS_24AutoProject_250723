import asyncio
import os
import sys
import sqlite3
import pytest

# ✅ modules 폴더를 import 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.account_runner import log_account_run, run_all_accounts

# ────────────────────────── 공통 FIXTURE: DB를 메모리로 ──────────────────────────
@pytest.fixture(autouse=True)
def _in_memory_db(monkeypatch):
    monkeypatch.setattr("modules.account_runner.DB_PATH", ":memory:")
    conn = sqlite3.connect(":memory:")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS account_run_log (
        session_id TEXT,
        account    TEXT,
        status     TEXT,
        message    TEXT
    )
    """)
    conn.commit()
    conn.close()
    yield

# ────────────────────────────── log_account_run 테스트 ─────────────────────────────
@pytest.mark.parametrize(
    "sid, acc, stat, msg",
    [
        ("SID1", "acc1", "success", "ok"),
        ("SID2", "acc2", "fail", "err"),
    ]
)
def test_log_account_run(sid, acc, stat, msg):
    result = log_account_run(sid, acc, stat, msg)
    assert result is None

# ────────────────────────────── run_all_accounts 테스트 ─────────────────────────────
def test_run_all_accounts(monkeypatch):
    # ✅ run_account 함수를 더미 함수로 교체해 테스트 가능하게 만듦
    async def dummy_run_account(account, session_id):
        return f"TEST-{account}"

    monkeypatch.setattr("modules.account_runner.run_account", dummy_run_account)

    # ✅ run_all_accounts를 직접 실행
    result = asyncio.run(run_all_accounts("SID_TEST"))
    assert result is None
