import sqlite3

conn = sqlite3.connect(r"./db/account_log.db")
cur = conn.cursor()
sql = cur.execute(
    "SELECT sql FROM sqlite_master WHERE type='table' AND name='account_run_log';"
).fetchone()[0]
print(sql)
