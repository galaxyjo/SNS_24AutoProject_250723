
import sqlite3
import pandas as pd
from datetime import datetime
conn = sqlite3.connect("db/network_log.db")
conn.close()
df = pd.read_sql_query("SELECT * FROM network_log", conn)
df.to_csv(filename, index=False)
filename = f"logs/export_network_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
print(f"✅ Export complete: {filename}")
