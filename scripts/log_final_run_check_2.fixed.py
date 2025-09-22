
latest_file = file
                    latest_time = mod_time
                file_path = os.path.join(LOG_DIR, file)
                if latest_time is None or mod_time > latest_time:
                mod_time = os.path.getmtime(file_path)
            if file.startswith(pattern):
            print(f"✔️ {log_type} → 최근 로그: {latest_file}")
            print(f"⚠️ {log_type} → 로그 없음 (생성 필요)")
        else:
        for file in os.listdir(LOG_DIR):
        if latest_file:
        latest_file = None
        latest_time = None
        pattern = f"{log_type}_"
    "final_runcheck",
    "logs_summary",
    "operational_plan",
    "qa_review",
    "README",
    "release_info",
    "session_integrity",
    check_recent_logs()
    for log_type in LOG_TYPES:
    print("✅ 최종 로그 점검 시작")
    print(f"\n📅 점검 완료: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
# 점검할 로그 디렉터리
]
def check_recent_logs():
from datetime import datetime

if __name__ == "__main__":
import os

LOG_DIR = "logs"
LOG_TYPES = [

pass
