
import sys
import sqlite3
import os
from dotenv import load_dotenv
cur.execute("ALTER TABLE users ADD COLUMN role TEXT")
print("??'role' 而щ읆 ?대? 議댁옱")
print("??'role' 而щ읆 異붽? ?꾨즺")
#
# -*- coding: utf-8 -*-
# role 而щ읆 議댁옱 ?щ? ?뺤씤
BASE_PATH = os.getenv("BASE_PATH")
columns = [col[1] for col in cur.fetchall()]
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("PRAGMA table_info(users);")
DB_PATH = os.getenv("DB_PATH")
db_path = os.path.join(os.path.dirname(__file__), "..", "db", "session_log.db")
else:
EXPORT_PATH = os.getenv("EXPORT_PATH")
if "role" not in columns:
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
sys.path.append(MODULE_PATH)
