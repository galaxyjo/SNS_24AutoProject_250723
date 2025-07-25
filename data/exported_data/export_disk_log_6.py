
# scripts/export_disk_log.py
import sqlite3
import pandas as pd
import os
from datetime import datetime
conn = sqlite3.connect("db/disk_log.db")
conn.close()
df = pd.read_sql_query("SELECT * FROM disk_log ORDER BY id DESC", conn)
df.to_csv(export_path, index=False, encoding="utf-8-sig")
export_path = os.path.join("logs", f"export_disk_log_{timestamp}.csv")
print(f"✅ Export complete: {export_path}")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
