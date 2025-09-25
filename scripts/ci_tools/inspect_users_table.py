
import os
import sqlite3

print("✅ users 테이블 존재 확인")
print("❌ users 테이블 없음 → 복구 필요")
# inspect_users_table.py
# 테이블 존재 여부 확인
conn = sqlite3.connect(db_path)
conn.close()
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "db",
    "user_credentials.db")
else:
if result:
result = cur.fetchone()

pass
