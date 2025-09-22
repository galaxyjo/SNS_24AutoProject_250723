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
print(f"✅ Export 완료 → {args.out}")
