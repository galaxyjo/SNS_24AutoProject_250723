# core/db.py

import os
import sqlite3
from decorators.log_trace import log_trace

@log_trace
def init_db():
    db_path = os.path.join("db", "trace_log.db")
    os.makedirs("db", exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS function_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            function_name TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

    print("✅ DB 초기화 완료")

# 함수 직접 실행
if __name__ == "__main__":
    init_db()
