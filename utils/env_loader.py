import os

from dotenv import load_dotenv


def load_env():
    dotenv_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print(f"✅ .env loaded from: {dotenv_path}")
    else:
        print("⚠️ .env file not found.")


def get_db_path():  # ✅ 여기 수정
    load_dotenv()
    base_dir = os.getenv("BASE_DIR", "")
    db_path = os.getenv("DB_PATH", "db/account_log.db")
    return os.path.join(base_dir, db_path)
