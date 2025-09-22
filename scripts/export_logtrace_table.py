# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
sys.path.append(MODULE_PATH)
os.chdir(BASE_PATH)
import argparse
import os
import sqlite3

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--table", required=True)
parser.add_argument("--db", required=True)
parser.add_argument("--out", required=True)
args = parser.parse_args()

conn = sqlite3.connect(args.db)
df = pd.read_sql_query(f"SELECT * FROM {args.table}", conn)
os.makedirs(os.path.dirname(args.out), exist_ok=True)
df.to_csv(args.out, index=False, encoding="utf-8-sig")
conn.close()
print(f"? Export 완료 → {args.out}")
