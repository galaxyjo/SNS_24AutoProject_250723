# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")
EXPORT_PATH = os.getenv("EXPORT_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
sys.path.append(MODULE_PATH)
os.chdir(BASE_PATH)
