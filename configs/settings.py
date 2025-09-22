# .env 파일 경로 설정 (.env는 clean_rebuild 루트에 위치)
# 환경변수 불러오기
import os

from dotenv import load_dotenv

BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)
LOG_EXPORT_PATH = os.getenv("LOG_EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
