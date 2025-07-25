
import sqlite3
import csv
from datetime import datetime
writer = csv.writer(f)
writer.writerow(headers)
writer.writerows(rows)
conn = sqlite3.connect("db/command_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM command_log ORDER BY executed_at DESC")
filename = f"logs/export_command_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
headers = [description[0] for description in cur.description]
print(f"✅ Export complete: {filename}")
rows = cur.fetchall()
with open(filename, mode="w", newline="", encoding="utf-8") as f:
