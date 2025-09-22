import sqlite3
import pytest
import asyncio
from modules.account_runner import run_all_accounts, init_log_db
from modules.log_trace import get_logger  # ✅ 경로 수정됨


def test_logger_runs():
    logger = get_logger()
    assert logger.name == "SNSLogger"


@pytest.mark.asyncio
async def test_run_all_accounts_logs(tmp_path):
    sess_id = "test_session"
    test_db_path = tmp_path / "test_account_log.db"

    # ✅ DB 연결 및 테이블 생성
    conn = init_log_db(db_path=str(test_db_path))

    # ✅ 커넥션을 명시적으로 전달 (비동기 실행 필요)
    await run_all_accounts(sess_id, conn=conn)

    # ✅ DB에 실제 로그가 저장되었는지 확인
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM account_run_log WHERE session_id = ?", (sess_id,)
    )
    count = cursor.fetchone()[0]
    assert count > 0
