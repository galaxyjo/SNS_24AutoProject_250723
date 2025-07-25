from dotenv import load_dotenv
import os

def load_env():
    dotenv_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print(f"✅ .env loaded from: {dotenv_path}")
    else:
        print("⚠️ .env file not found.")
