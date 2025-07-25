
        all_exist = False
        print(f"???뚯씪 ?놁쓬: {full_path}")
        print(f"???뚯씪 議댁옱 ?뺤씤: {full_path}")
    "missing_field_summary.csv",
    "qa_session_check_{}.csv".format(datetime.now().strftime("%Y%m%d")),
    else:
    full_path = os.path.join(base_path, file)
    if os.path.exists(full_path):
    print("?렞 紐⑤뱺 濡쒓렇 ?뺤씤 ?꾨즺 ??WT-07 ?깃났")
    print("?좑툘 ?쇰? ?뚯씪 ?꾨씫 ??WT-07 ?먭? ?꾩슂")
# -*- coding: utf-8 -*-
]
all_exist = True
base_path = "logs/qa"
BASE_PATH = os.getenv("BASE_PATH")
DB_PATH = os.getenv("DB_PATH")
else:
expected_files = [
EXPORT_PATH = os.getenv("EXPORT_PATH")
for file in expected_files:
from datetime import datetime
from dotenv import load_dotenv
if all_exist:
import os
import sys
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
LOG_PATH = os.getenv("LOG_PATH")
MODULE_PATH = os.getenv("MODULE_PATH")
os.chdir(BASE_PATH)
print("[WT-07-S6~S8] ?ㅽ뻾寃곌낵 ?뺤씤")
sys.path.append(MODULE_PATH)
