import os
import sqlite3
import pytest
from modules import log_trace


@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / "test_log.db"
    conn = sqlite3.connect(db_path)
    yield conn
    conn.close()


def test_init_log_db_creates_tables(temp_db):
    conn = temp_db
    log_trace.init_log_db(conn=conn)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cursor.fetchall()}
    assert "session_log" in tables
    assert "account_run_log" in tables


def test_insert_session_log_and_retrieve(temp_db):
    conn = temp_db
    log_trace.init_log_db(conn=conn)
    sess_id = "test_sess_123"
    run_at = log_trace.get_run_at_timestamp()
    status = "TEST"
    # ✅ 순서: sess_id, run_at, status
    log_trace.insert_session_log(sess_id, run_at, status, conn=conn)
    cursor = conn.cursor()
    cursor.execute("SELECT session_id, run_at, status FROM session_log")
    rows = cursor.fetchall()
    assert rows[0][0] == sess_id
    assert rows[0][1] == run_at
    assert rows[0][2] == status


def test_insert_account_run_log(temp_db):
    conn = temp_db
    log_trace.init_log_db(conn=conn)
    sess_id = "sess_test"
    acc = "acc01"
    success = True
    run_at = log_trace.get_run_at_timestamp()
    log_trace.insert_account_run_log(sess_id, acc, success, run_at, conn=conn)
    cursor = conn.cursor()
    cursor.execute("SELECT session_id, account, status, ts FROM account_run_log")
    row = cursor.fetchone()
    assert row == (sess_id, acc, "SUCCESS", run_at)
