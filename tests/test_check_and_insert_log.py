import sqlite3
import pytest

from validator.check_and_insert_log import (
    ensure_logs_table,
    insert_test_log,
    fetch_all_logs,
    get_log_count
)

@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / "test_log.db"
    conn = sqlite3.connect(db_path)
    # 직접 logs 테이블 생성
    conn.execute("""
        CREATE TABLE logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            message TEXT,
            session_id TEXT
        )
    """)
    conn.commit()
    yield conn
    conn.close()

def test_ensure_logs_table_creates_table(temp_db):
    ensure_logs_table(temp_db)

def test_insert_log(temp_db):
    insert_test_log(temp_db)
    assert get_log_count(temp_db) == 1

def test_multiple_logs(temp_db):
    insert_test_log(temp_db)
    insert_test_log(temp_db)
    assert get_log_count(temp_db) == 2

def test_fetch_logs(temp_db):
    insert_test_log(temp_db)
    logs = fetch_all_logs(temp_db)
    assert len(logs) == 1
    assert logs[0][2] == "INFO"  # level 필드 확인
