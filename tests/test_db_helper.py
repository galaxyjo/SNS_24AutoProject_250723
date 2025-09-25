# tests/test_db_helper.py
import os
import sqlite3
import tempfile
import pytest
from modules.common import db_helper


@pytest.fixture
def temp_db():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()
    conn = db_helper.get_db_connection(tmp.name)
    yield conn
    conn.close()
    os.unlink(tmp.name)


def test_init_and_insert_logs(temp_db):
    db_helper.init_logs_table(temp_db)
    db_helper.insert_log(temp_db, "2025-09-24 12:00:00", "INFO", "Test message", "sess1")
    logs = db_helper.fetch_all_logs(temp_db)
    assert len(logs) == 1
    assert logs[0][2] == "INFO"
    assert logs[0][3] == "Test message"


def test_init_and_insert_log_trace(temp_db):
    db_helper.init_log_trace_table(temp_db)
    db_helper.insert_log_trace(
        temp_db, "file.py", "func", "desc", "GPT_REF_1", "STEP_1"
    )
    traces = db_helper.fetch_all_log_traces(temp_db)
    assert len(traces) == 1
    assert traces[0][1] == "file.py"
    assert traces[0][2] == "func"
    assert traces[0][3] == "desc"
