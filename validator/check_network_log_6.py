import sqlite3

from tabulate import tabulate

conn = sqlite3.connect("db/network_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM network_log")
headers = [description[0] for description in cur.description]
print(tabulate(rows, headers=headers, tablefmt="grid"))
rows = cur.fetchall()
