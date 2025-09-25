# scripts/upgrade_users_add_role_2.py (정상화/디버깅 버전)
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "session_log.db")


def ensure_role_column(db_path: str = DB_PATH) -> None:
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"⚠️ DB 파일 없음: {db_path}")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(users);")
    columns = [col[1] for col in cur.fetchall()]

    if "role" not in columns:
        cur.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'viewer'")
        print("✅ role 컬럼 추가 완료 (기본값: viewer)")
    else:
        print("✅ role 컬럼 이미 존재함")

    cur.execute("UPDATE users SET role='admin' WHERE username='admin'")
    print("✅ admin 계정 role='admin' 설정 완료")

    conn.commit()
    conn.close()


def main():
    ensure_role_column()


if __name__ == "__main__":
    main()
