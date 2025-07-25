
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
]
all_exist = True
base_path = "logs/qa"
else:
expected_files = [
for file in expected_files:
from datetime import datetime
if all_exist:
import os
print("[WT-07-S6~S8] 실행결과 확인")
