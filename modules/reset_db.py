import sqlite3

conn = sqlite3.connect('db/account_log.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS account_run_log')
cursor.execute('''
CREATE TABLE account_run_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    account TEXT,
    status TEXT,
    message TEXT,
    run_at TEXT
)
''')
conn.commit()
conn.close()

print("✅ account_run_log 테이블 재생성 완료")
