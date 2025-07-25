
# -*- coding: utf-8 -*-
import sys
import os
from dotenv import load_dotenv
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
sys.path.append(MODULE_PATH)
