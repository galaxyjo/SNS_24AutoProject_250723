
conn = sqlite3.connect("db/network_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM network_log")
from tabulate import tabulate
headers = [description[0] for description in cur.description]
import sqlite3
print(tabulate(rows, headers=headers, tablefmt="grid"))
rows = cur.fetchall()
