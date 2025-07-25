
    cur.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'viewer'")
    print("✅ role 컬럼 이미 존재함")
    print("✅ role 컬럼 추가 완료 (기본값: viewer)")
# role 컬럼 존재 여부 확인
# 기본 admin 계정의 role을 'admin'으로 업데이트
# 저장 위치: C:\SNS_24AutoProject\scripts\upgrade_users_add_role.py
# 파일명: upgrade_users_add_role.py
columns = [col[1] for col in cur.fetchall()]
conn = sqlite3.connect(db_path)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute("PRAGMA table_info(users);")
cur.execute("UPDATE users SET role='admin' WHERE username='admin'")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "session_log.db")
else:
if "role" not in columns:
import os
import sqlite3
print("✅ admin 계정 role='admin' 설정 완료")
