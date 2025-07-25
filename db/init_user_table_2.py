
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT,
        role TEXT DEFAULT 'viewer'
        username TEXT UNIQUE,
    """
    "INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)",
    ("admin", "1234", "admin"),
    );
    CREATE TABLE IF NOT EXISTS users (
"""
# admin 계정 등록
# users 테이블 생성
# 목적: user_credentials.db에 users 테이블 생성 및 admin 계정 등록
# 절대 경로 기준 DB 연결
# 파일명: init_user_table.py
)
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute(
db_path = os.path.join(base_path, "db", "user_credentials.db")
import os
import sqlite3
print("✅ users 테이블 생성 및 기본 계정 등록 완료 (user_credentials.db)")
