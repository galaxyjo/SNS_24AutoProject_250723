import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_db_path() -> str:
    return os.getenv("TRACE_LOG_DB") or os.path.abspath("db/trace_log.db")

def ensure_db_exists(db_path: str) -> None:
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"⚠️ DB 파일이 존재하지 않음: {db_path}")
    print(f"✅ DB 파일 존재 확인: {db_path}")

def ensure_logs_table(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            message TEXT,
            session_id TEXT
        )
    """)
    conn.commit()
    print("✅ logs 테이블 존재 확인")

def insert_test_log(conn: sqlite3.Connection, session_id: str = "session_test") -> None:
    cur = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(
        "INSERT INTO logs (timestamp, level, message, session_id) VALUES (?, ?, ?, ?)",
        (timestamp, "INFO", "테스트 로그", session_id)
    )
    conn.commit()
    print("✅ 로그 삽입 완료")

def get_log_count(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0]

def fetch_all_logs(conn: sqlite3.Connection) -> list:
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs")
    return cur.fetchall()

def main():
    db_path = get_db_path()
    ensure_db_exists(db_path)
    conn = sqlite3.connect(db_path)
    try:
        ensure_logs_table(conn)
        insert_test_log(conn)
        logs = fetch_all_logs(conn)
        print("📋 로그 리스트:", logs)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
