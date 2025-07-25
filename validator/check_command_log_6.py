
conn = sqlite3.connect("db/command_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM command_log ORDER BY executed_at DESC")
from tabulate import tabulate
headers = [description[0] for description in cur.description]
import sqlite3
print(tabulate(rows, headers=headers, tablefmt="grid"))
rows = cur.fetchall()
