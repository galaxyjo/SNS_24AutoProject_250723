
import sqlite3
import pandas as pd
conn = sqlite3.connect("db/trace_log.db")
df = pd.read_sql_query("SELECT * FROM log_trace", conn)
df.to_csv("logs/export_logtrace.csv", index=False)
print("? �α� CSV ���� �Ϸ�")
