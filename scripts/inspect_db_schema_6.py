
                print(f" - {col[1]} ({col[2]})")
            columns = cursor.fetchall()
            cursor.execute(f"PRAGMA table_info({table_name})")
            for col in columns:
            print("No tables found.")
            print(f"\n[TABLE] {table_name}")
            return
        conn = sqlite3.connect(db_path)
        conn.close()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for (table_name,) in tables:
        if not tables:
        inspect_db_schema(db)
        print(f"[ERROR] Failed to inspect {db_path}: {e}")
        print(f"[ERROR] File not found: {db_path}")
        print(f"\n=== {db_path} ===")
        return
        tables = cursor.fetchall()
    except Exception as e:
    finally:
    for db in DB_FILES:
    if not os.path.exists(db_path):
    try:
DB_FILES = ["db/trace_log.db", "db/session_log.db", "db/env_log.db"]
def inspect_db_schema(db_path):
if __name__ == "__main__":
import os
import sqlite3
