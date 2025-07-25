
# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
conn = sqlite3.connect("db/trace_log.db")
df = pd.read_sql_query("SELECT * FROM log_trace", conn)
df.to_csv("logs/export_logtrace.csv", index=False)
print("? 로그 CSV 저장 완료")
