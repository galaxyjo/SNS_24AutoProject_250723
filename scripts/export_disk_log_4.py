# scripts/export_disk_log.py
import os
import sqlite3
from datetime import datetime

import pandas as pd

conn = sqlite3.connect("db/disk_log.db")
df = pd.read_sql_query("SELECT * FROM disk_log ORDER BY id DESC", conn)
conn.close()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
export_path = os.path.join("logs", f"export_disk_log_{timestamp}.csv")
df.to_csv(export_path, index=False, encoding="utf-8-sig")

print(f"✅ Export complete: {export_path}")
