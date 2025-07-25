
# scripts\check_disk_log.py
conn = sqlite3.connect("db/disk_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM disk_log ORDER BY id DESC")
from tabulate import tabulate
headers = [description[0] for description in cur.description]
import sqlite3
print(tabulate(rows, headers=headers, tablefmt="grid"))
rows = cur.fetchall()
