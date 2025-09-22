
import os
import sqlite3

"INSERT OR IGNORE INTO users (username, password, role) VALUES ('viewer1', 'test1234', 'viewer')"
# 위치: C:\SNS_24AutoProject\scripts\insert_viewer_user.py
# 파일명: insert_viewer_user.py
)
    conn = sqlite3.connect(db_path)
    conn.close()
    conn.commit()
    cur = conn.cursor()
    cur.execute(
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "session_log.db")
print("✅ viewer1 계정 생성 완료 (비밀번호: test1234, 권한: viewer)")

pass
