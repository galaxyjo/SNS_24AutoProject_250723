# tests/test_verify_session_integrity_6.py
import os
import sqlite3
import tempfile
import pandas as pd
import pytest
from scripts import verify_session_integrity_6 as vsi

@pytest.fixture
def temp_dbs():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_paths = {}
        for name in vsi.DB_FILES:
            path = os.path.join(tmpdir, f"{name}.db")
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS session_table (
                    session_id TEXT PRIMARY KEY
                )
            """)
            cursor.execute("INSERT INTO session_table (session_id) VALUES (?)", ("abc123",))
            conn.commit()
            conn.close()
            db_paths[name] = path
        yield db_paths

def test_load_session_ids(temp_dbs):
    for name, path in temp_dbs.items():
        ids = vsi.load_session_ids(path)
        assert "abc123" in ids

def test_main_creates_output_files(monkeypatch, temp_dbs):
    monkeypatch.setattr(vsi, "DB_FILES", temp_dbs)
    vsi.main()
    assert os.path.exists(vsi.OUTPUT_CSV)
