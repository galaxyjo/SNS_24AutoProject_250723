# modules/common/import_csv_to_db.py
import os
import sqlite3
import csv
from typing import Optional


def get_db_path() -> str:
    base_dir = os.getenv("BASE_PATH") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "logs", "trace_log.db")


def get_csv_path(filename: str) -> str:
    base_dir = os.getenv("BASE_PATH") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "logs", filename)


def init_table(conn: sqlite3.Connection, table_name: str):
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            function_name TEXT,
            desc TEXT,
            GPT_REF TEXT,
            STEP TEXT,
            inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()


def import_csv_to_db(csv_filename: str, table_name: str = "log_trace", db_path: Optional[str] = None) -> int:
    db_path = db_path or get_db_path()
    csv_path = get_csv_path(csv_filename)

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"⚠️ CSV not found: {csv_path}")

    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    conn = sqlite3.connect(db_path)
    init_table(conn, table_name)

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [
            (
                r.get("file_name", ""),
                r.get("function_name", ""),
                r.get("desc", ""),
                r.get("GPT_REF", ""),
                r.get("STEP", "")
            ) for r in reader
        ]

    cur = conn.cursor()
    cur.executemany(f"""
        INSERT INTO {table_name} (file_name, function_name, desc, GPT_REF, STEP)
        VALUES (?, ?, ?, ?, ?)
    """, rows)
    conn.commit()
    conn.close()

    print(f"✅ Inserted {len(rows)} rows into {table_name}")
    return len(rows)


def main():
    import_csv_to_db("insert_log_2025-05-01.csv")


if __name__ == "__main__":
    main()
