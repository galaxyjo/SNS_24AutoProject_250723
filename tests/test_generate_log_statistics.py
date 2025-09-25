# tests/test_generate_log_statistics.py

import os
import tempfile
import sqlite3
import pandas as pd

from scripts.generate_log_statistics import fetch_log_statistics

def test_fetch_log_statistics_basic():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "temp_log.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create mock table
        cursor.execute("""
        CREATE TABLE command_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            executed_at TEXT,
            command TEXT
        )""")
        cursor.execute("INSERT INTO command_log (executed_at, command) VALUES (?, ?)", ("2025-09-24 23:59:00", "echo test"))
        conn.commit()
        conn.close()

        result = fetch_log_statistics(db_path=db_path, tables=["command_log"])
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["table"] == "command_log"
        assert result[0]["row_count"] == 1
        assert "command" in result[0]["columns"]
