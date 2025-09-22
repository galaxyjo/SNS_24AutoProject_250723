import csv
import sqlite3
from datetime import datetime

conn = sqlite3.connect("db/env_log.db")
cur = conn.cursor()

cur.execute("SELECT * FROM env_log ORDER BY created_at DESC")
rows = cur.fetchall()
headers = [description[0] for description in cur.description]

filename = f"logs/export_env_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ Export complete: {filename}")
conn.close()
