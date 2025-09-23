# -*- coding: utf-8 -*-
"""
Export all log tables to Excel
- Uses DB_PATH and EXPORT_PATH from .env
- Automatically detects available tables
"""

import os
import sys
import sqlite3
import pandas as pd
from dotenv import load_dotenv

# Load environment
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")

# Default fallback if not defined
if not DB_PATH:
    DB_PATH = os.path.join(BASE_PATH, "db", "account_log.db")
if not EXPORT_PATH:
    EXPORT_PATH = os.path.join(BASE_PATH, "logs", "export_all_logtables.xlsx")

# Ensure working dir
os.chdir(BASE_PATH)
sys.path.append(BASE_PATH)


def export_all_tables_to_excel(db_path: str, export_path: str) -> None:
    """Export all tables in sqlite DB to Excel."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"DB not found: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    if not tables:
        raise RuntimeError("No tables found in DB")

    with pd.ExcelWriter(export_path, engine="xlsxwriter") as writer:
        for table in tables:
            try:
                df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
                df.to_excel(
                    writer, sheet_name=table[:31], index=False
                )  # Excel sheet limit = 31 chars
            except Exception as e:
                print(f"⚠️ Failed to export table {table}: {e}")

    conn.close()
    print(f"✅ Export complete → {export_path}")


if __name__ == "__main__":
    export_all_tables_to_excel(DB_PATH, EXPORT_PATH)
