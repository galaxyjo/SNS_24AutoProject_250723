
all_exist = False
        print(f"✅ 파일 존재 확인: {full_path}")
        print(f"❌ 파일 없음: {full_path}")
    "missing_field_summary.csv",
    "qa_session_check_{}.csv".format(datetime.now().strftime("%Y%m%d")),
    else:
    full_path = os.path.join(base_path, file)
    if os.path.exists(full_path):
    print("⚠️ 일부 파일 누락 → WT-07 점검 필요")
    print("🎯 모든 로그 확인 완료 → WT-07 성공")
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
