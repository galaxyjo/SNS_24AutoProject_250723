# tests/test_hook_status_logger.py

import os
import sqlite3
import pytest
from modules.common.hook_status_logger import init_db, log_status, DB_PATH

@pytest.fixture(autouse=True)
def setup_and_teardown():
    test_db_path = DB_PATH.replace("hook_status.db", "test_hook_status.db")
    if os.path.exists(test_db_path):
        os.remove(test_db_path)
    yield test_db_path
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

def test_init_db_creates_table(setup_and_teardown):
    test_db = setup_and_teardown
    init_db(test_db)
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hook_logs'")
    table = cursor.fetchone()
    conn.close()
    assert table is not None

def test_log_status_inserts_data(setup_and_teardown):
    test_db = setup_and_teardown
    init_db(test_db)
    log_status("OK", "test reason", test_db)
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("SELECT status, reason FROM hook_logs ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    assert row == ("OK", "test reason")
