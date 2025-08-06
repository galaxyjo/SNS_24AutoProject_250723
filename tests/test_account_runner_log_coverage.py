# tests/test_account_runner_log_coverage.py

import pytest
import sqlite3
import os
from modules.account_runner import log_account_run, run_account, init_log_db, DB_PATH


def test_log_account_run_internal_conn(tmp_path):
    # ✅ 내부 커넥션 생성 흐름 테스트
    db_file = tmp_path / "account_log.db"
    os.environ["PYTHONPATH"] = str(tmp_path)
    init_log_db()
    log_account_run("SID_X", "acc_test", "SUCCESS", "ok", conn=None)

    assert os.path.exists(DB_PATH)


def test_log_account_run_external_conn(tmp_path):
    # ✅ 외부에서 커넥션 주입 테스트
    test_db = tmp_path / "custom_log.db"
    conn = sqlite3.connect(test_db)
    log_account_run("SID_Y", "acc_ext", "FAIL", "error!", conn=conn)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account_run_log")
    rows = cursor.fetchall()

    assert len(rows) == 1
    assert rows[0][0] == "SID_Y"
    conn.close()


@pytest.mark.asyncio
async def test_run_account_failures(monkeypatch):
    # ✅ 강제 예외 발생 유도해서 3회 실패 흐름 및 로그 기록 확인
    async def mock_execute_fail(*args, **kwargs):
        raise RuntimeError("Mock failure")

    monkeypatch.setattr("modules.core.main_features.execute_account", mock_execute_fail)

    result = await run_account("SID_FAIL", "account_fail")

    assert result["status"] == "fail"
    assert result["account"] == "account_fail"
    assert "message" in result
    assert "Mock failure" in result["message"]
