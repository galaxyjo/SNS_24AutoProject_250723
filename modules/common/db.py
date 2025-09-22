# db.py

import os
import sqlite3

from decorators.log_trace import log_trace


@log_trace
def init_db():
    db_path = os.path.join("db", "trace_log.db")
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 예시 테이블 생성 (없을 시)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS function_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            function_name TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()
    conn.close()
    print("✅ DB 초기화 완료")
