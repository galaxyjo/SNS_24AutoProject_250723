# -*- coding: utf-8 -*-
"""
Export all tables from SQLite DB to Excel with datetime suffix.
- Uses DB_PATH and EXPORT_PATH from .env
- Creates timestamped filename automatically
"""

import os
import sys
import sqlite3
import datetime
import pandas as pd
from dotenv import load_dotenv

# Load environment
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

BASE_PATH = os.getenv("BASE_PATH", BASE_DIR)
DB_PATH = os.getenv("DB_PATH")
EXPORT_DIR = os.getenv("EXPORT_PATH")

# Default fallback if not defined
if not DB_PATH:
    DB_PATH = os.path.join(BASE_PATH, "db", "account_log.db")
if not EXPORT_DIR:
    EXPORT_DIR = os.path.join(BASE_PATH, "logs", "exports")

os.makedirs(EXPORT_DIR, exist_ok=True)

# Ensure working dir
os.chdir(BASE_PATH)
sys.path.append(BASE_PATH)


def export_all_tables_with_datetime(db_path: str, export_dir: str) -> str:
    """Export all tables in SQLite DB to Excel, filename with datetime suffix."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"DB not found: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    if not tables:
        raise RuntimeError("No tables found in DB")

    export_path = os.path.join(
        export_dir,
        f"export_all_tables_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
    )

    # Pick Excel engine dynamically
    engine = "xlsxwriter"
    try:
        __import__("xlsxwriter")
    except ImportError:
        engine = "openpyxl"

    with pd.ExcelWriter(export_path, engine=engine) as writer:
        for table in tables:
            try:
                df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
                df.to_excel(
                    writer, sheet_name=table[:31], index=False
                )  # Excel limit 31 chars
            except Exception as e:
                print(f"⚠️ Failed to export table {table}: {e}")

    conn.close()
    print(f"✅ Export complete → {export_path}")
    return export_path


def main():
    export_all_tables_with_datetime(DB_PATH, EXPORT_DIR)


if __name__ == "__main__":
    main()
