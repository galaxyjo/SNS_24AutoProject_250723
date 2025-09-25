# tests/test_send_log_webhook_2.py (수정/디버깅 완료)
import pytest
import sqlite3
import tempfile
import os
from scripts import send_log_webhook_2 as slw
from unittest.mock import patch


@pytest.fixture
def temp_db():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "trace_log.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE logs (id INTEGER PRIMARY KEY, timestamp TEXT, message TEXT)"
        )
        cursor.execute(
            "INSERT INTO logs (timestamp, message) VALUES (?, ?)",
            ("2025-09-24T12:00:00", "test log"),
        )
        conn.commit()
        conn.close()
        yield db_path


def test_send_latest_log_success(temp_db):
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"ok": True}
        response = slw.send_latest_log(
            db_path=temp_db, webhook_url="http://example.com"
        )
        assert response.status_code == 200


def test_send_latest_log_no_logs(temp_db):
    # empty table
    conn = sqlite3.connect(temp_db)
    conn.execute("DELETE FROM logs")
    conn.commit()
    conn.close()
    response = slw.send_latest_log(db_path=temp_db, webhook_url="http://example.com")
    assert response is None
