
import sqlite3

import pandas as pd

print("⚠️ No environment log data found.")
print(df.to_markdown(index=False))
conn = sqlite3.connect("db/env_log.db")
conn.close()
df = pd.read_sql_query("SELECT * FROM env_log ORDER BY created_at DESC", conn)
else:
if df.empty:
