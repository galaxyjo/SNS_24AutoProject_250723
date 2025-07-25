
        count = cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        f.write(f"{table_name}, {count}\n")
        table_name = table[0]
    + ".csv"
    + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    f.write("Table Name, Row Count\n")
    for table in tables:
    r"C:\BackUp_ehcho_galaxy\logs\log_summary_"
)
conn = sqlite3.connect(DB_PATH)
conn.close()
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_PATH = (
import datetime
import sqlite3
tables = cur.fetchall()
with open(EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
