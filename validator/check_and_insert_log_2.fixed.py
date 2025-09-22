
id INTEGER PRIMARY KEY AUTOINCREMENT,
            level TEXT,
            message TEXT,
            session_id TEXT
            timestamp TEXT,
        """
        );
        CREATE TABLE logs (
    """
    )
    cur.execute(
    INSERT INTO logs (timestamp, level, message, session_id)
    print("✅ logs 테이블 생성 완료")
    print("✅ logs 테이블 존재 확인")
    print(row)
    VALUES ('2025-05-05 21:30:00', 'INFO', 'Streamlit 테스트 로그 삽입', 'session_test')
"""
# 1. DB 연결
# 2. logs 테이블 존재 여부 확인
# 3. 레코드 개수 조회
# 4. 테스트 로그 1건 삽입
# 5. 전체 로그 출력
# 파일 위치: C:\SNS_24AutoProject\scripts\check_and_insert_log.py
)
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
count = cur.fetchone()[0]
cur = conn.cursor()
cur.execute(
cur.execute("SELECT * FROM logs;")
cur.execute("SELECT COUNT(*) FROM logs;")
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='logs';")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "trace_log.db")
else:
for row in rows:
if not cur.fetchone():
import os
import sqlite3
print("✅ 테스트 로그 삽입 완료")
print("📋 전체 로그:")
print(f"📦 현재 로그 레코드 수: {count}")
rows = cur.fetchall()

pass
