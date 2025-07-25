
import sys
import sqlite3
import os
import csv
from dotenv import load_dotenv
from datetime import datetime
writer = csv.writer(f)
writer.writerow(headers)
writer.writerows(rows)
# -*- coding: utf-8 -*-
BASE_PATH = os.getenv("BASE_PATH")
conn = sqlite3.connect("db/command_log.db")
conn.close()
cur = conn.cursor()
cur.execute("SELECT * FROM command_log ORDER BY executed_at DESC")
DB_PATH = os.getenv("DB_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
filename = f"logs/export_command_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
headers = [description[0] for description in cur.description]
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print(f"??Export complete: {filename}")
rows = cur.fetchall()
sys.path.append(MODULE_PATH)
with open(filename, mode="w", newline="", encoding="utf-8") as f:
