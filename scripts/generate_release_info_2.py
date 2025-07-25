
    f"docs/release_info_{datetime.now().strftime('%Y%m%d')}.md", "w", encoding="utf-8"
    f.write(release_info)
- dashboards\\dashboard_full_tabs.py
- db\\trace_log.db, user_credentials.db
- decorators\\log_trace.py
- logs\\ (백업, export, 최종기록 포함)
- main.py
- modules\\account_runner.py, db.py, utils.py, logger.py
- scripts\\ (모든 자동화 스크립트 포함)
"""
# C:\SNS_24AutoProject\scripts\generate_release_info.py
) as f:
✅ 전체 시스템은 완전 자동화되어 있으며, Streamlit + PowerShell + SQLite 기반으로 작동합니다.
from datetime import datetime
import os
os.makedirs("docs", exist_ok=True)
print("✅ Release Info 생성 완료")
release_info = f"""# 🚀 Release Info
with open(
📅 생성일: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📦 경로: C:\\SNS_24AutoProject
🛠 포함 모듈:
