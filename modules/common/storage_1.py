import os
import sqlite3
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.getenv("DB_PATH", os.path.join(BASE_DIR, "db", "session.db"))


def ensure_db_initialized(db_path: str = DB_PATH) -> None:
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS storage_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()


def insert_storage_data(key: str, value: str, db_path: str = DB_PATH) -> None:
    if not key or not value:
        raise ValueError("Key and Value must be non-empty strings.")

    ensure_db_initialized(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO storage_info (key, value) VALUES (?, ?);",
        (key, value)
    )
    conn.commit()
    conn.close()
    print(f"✅ Storage data inserted: {key} → {value}")


def get_storage_value(key: str, db_path: str = DB_PATH) -> Optional[str]:
    if not key:
        raise ValueError("Key must be a non-empty string.")

    if not os.path.exists(db_path):
        print("⚠️ DB file not found.")
        return None

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM storage_info WHERE key = ?;", (key,))
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None


def main():
    insert_storage_data("test_key", "test_value")
    value = get_storage_value("test_key")
    print(f"✅ Retrieved value: {value}")


if __name__ == "__main__":
    main()
