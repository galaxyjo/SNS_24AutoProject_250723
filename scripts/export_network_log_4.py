import sqlite3
from datetime import datetime

import pandas as pd

conn = sqlite3.connect("db/network_log.db")
df = pd.read_sql_query("SELECT * FROM network_log", conn)
filename = f"logs/export_network_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(filename, index=False)
print(f"✅ Export complete: {filename}")
conn.close()
