# tests/test_import_csv_to_db.py

import os
import sqlite3
import pandas as pd
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = os.getenv("BASE_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
CSV_PATH = os.path.join(BASE_PATH, "logs", "sample.csv")
DB_PATH = os.path.join(BASE_PATH, "db", "test_csv_import.db")
TABLE_NAME = "test_data"

def import_csv_to_db(csv_path: str, db_path: str, table_name: str):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"⚠️ CSV not found: {csv_path}")
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
    print(f"✅ CSV import 완료: {csv_path} → {table_name}")

@pytest.fixture(autouse=True)
def cleanup_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

def test_import_csv_to_db_inserts_data():
    import_csv_to_db(CSV_PATH, DB_PATH, TABLE_NAME)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    count = cursor.fetchone()[0]
    conn.close()
    assert count > 0
