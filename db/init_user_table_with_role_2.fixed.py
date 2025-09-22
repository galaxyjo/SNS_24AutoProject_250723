
import os
import sqlite3

cur.execute("ALTER TABLE users ADD COLUMN role TEXT")
print("✅ 'role' 컬럼 이미 존재")
print("✅ 'role' 컬럼 추가 완료")
#
# role 컬럼 존재 여부 확인
columns = [col[1] for col in cur.fetchall()]
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("PRAGMA table_info(users);")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "session_log.db")
else:
if "role" not in columns:
