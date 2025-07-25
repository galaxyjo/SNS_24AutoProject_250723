
# -*- coding: utf-8 -*-
import sys
import shutil
import os
import datetime
from dotenv import load_dotenv
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
DB_PATH = r"C:\BackUp_ehcho_galaxy\logs\trace_log.db"
EXPORT_DIR = r"C:\BackUp_ehcho_galaxy\logs\backup_exports"
EXPORT_PATH = os.getenv("EXPORT_PATH")
export_path = os.path.join(EXPORT_DIR, f"trace_log_backup_{timestamp}.db")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
os.makedirs(EXPORT_DIR, exist_ok=True)
shutil.copy2(DB_PATH, export_path)
sys.path.append(MODULE_PATH)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
