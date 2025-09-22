# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect(DB_PATH)
conn.close()
conn.commit()
cur = conn.cursor()
cur.execute("VACUUM")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
