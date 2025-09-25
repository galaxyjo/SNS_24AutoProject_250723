# tests/test_upgrade_users_add_role_2.py
import os
import sqlite3
import tempfile
import pytest
from scripts import upgrade_users_add_role_2 as upgr


@pytest.fixture
def temp_db():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "session_log.db")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE users (
                username TEXT PRIMARY KEY
            )
        """)
        cur.execute("INSERT INTO users (username) VALUES ('admin')")
        conn.commit()
        conn.close()
        yield db_path


def test_ensure_role_column_adds_role(temp_db):
    upgr.ensure_role_column(db_path=temp_db)
    conn = sqlite3.connect(temp_db)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(users);")
    columns = [col[1] for col in cur.fetchall()]
    assert "role" in columns
    cur.execute("SELECT role FROM users WHERE username='admin'")
    role = cur.fetchone()[0]
    conn.close()
    assert role == "admin"


def test_ensure_role_column_idempotent(temp_db):
    # 두 번 실행해도 오류 없어야 함
    upgr.ensure_role_column(db_path=temp_db)
    upgr.ensure_role_column(db_path=temp_db)
    conn = sqlite3.connect(temp_db)
    cur = conn.cursor()
    cur.execute("SELECT role FROM users WHERE username='admin'")
    role = cur.fetchone()[0]
    conn.close()
    assert role == "admin"
