
            """
            (commit_hash, author, date, message, datetime.now().isoformat()),
            [git_path, "log", "--pretty=format:%H|%an|%ad|%s"],
            author TEXT,
            commit_hash TEXT,
            continue
            date TEXT,
            encoding="utf-8",
            errors="ignore",  # cp949 충돌 회피
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            INSERT INTO git_log (commit_hash, author, date, message, inserted_at)
            inserted_at TEXT
            message TEXT,
            print("Git Error:", result.stderr)
            print("Git stdout is empty.")
            return []
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            VALUES (?, ?, ?, ?, ?)
        """
        """,
        )
        commit_hash, author, date, message = parts
        conn.close()
        CREATE TABLE IF NOT EXISTS git_log (
        cur.execute(
        if len(parts) != 4:
        if not result.stdout:
        if result.returncode != 0:
        lines = result.stdout.strip().split("\n")
        parts = line.split("|")
        print("❌ Git not found.")
        print("❌ Git 로그 없음. 삽입 생략.")
        print("Subprocess Exception:", e)
        print(f"❌ DB 파일이 존재하지 않습니다: {db_path}")
        result = subprocess.run(
        return
        return []
        return lines
    """
    # Git 실행파일 경로 확인
    )
    conn = sqlite3.connect(db_path)
    conn.close()
    conn.commit()
    cur = conn.cursor()
    cur.execute(
    except Exception as e:
    for line in logs:
    git_path = shutil.which("git")
    if git_path is None:
    if not logs:
    if not os.path.exists(db_path):
    insert_git_log_to_db()
    logs = get_git_log()
    print("✅ Git 로그 삽입 완료")
    try:
def get_git_log():
def insert_git_log_to_db(db_path="db/trace_log.db"):
from datetime import datetime
if __name__ == "__main__":
import os
import shutil
import sqlite3
import subprocess
