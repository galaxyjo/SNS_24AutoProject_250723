
---
    f.write(manual_text)
- admin / viewer1 계정 로그인
- decorators\\log_trace.py: 로그 데코레이터
- Excel 보고서: logs_summary_*.xlsx
- Export 버튼: 관리자만 노출됨
- Git 연동: scripts\\auto_send_gitlog_webhook.py
- modules\\account_runner.py: 계정 실행 처리
- modules\\db.py: SQLite DB 연동
- PowerShell: scripts\\final_backup_YYYYMMDD.ps1 실행
- URL: http://localhost:8501
- Webhook 전송: scripts\\send_log_webhook.py
- 로그 CSV: export_logtrace_*.csv
- 로그 시각화 / 통계 보기
- 세션 기반 필터링 자동 적용
- 실행: streamlit run dashboards\\dashboard_full_tabs.py
- 출력 경로: C:\\backup_YYYYMMDD_HHMM + .zip
"""
# C:\SNS_24AutoProject\scripts\generate_manuals.py
# 파일 저장
## 👤 3. 사용자 매뉴얼
## 👨‍💻 2. 개발자 매뉴얼
## 📌 1. 운영자 매뉴얼
### 기능
### 로그 추출
### 로그인
### 백업
### 외부 연동
### 주요 모듈 경로
✅ 완성 기준: WT-01 ~ WT-FINAL-BACKUP 전체 수행 결과 기반
from datetime import datetime
import os
manual_text = f"""# 🛠 운영자 · 개발자 · 사용자 매뉴얼
os.makedirs("docs", exist_ok=True)
output_path = os.path.join("docs", f"manuals_{datetime.now().strftime('%Y%m%d')}.md")
print(f"✅ 매뉴얼 생성 완료: {output_path}")
with open(output_path, "w", encoding="utf-8") as f:
📁 프로젝트: SNS_24AutoProject
📅 생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🗂 버전: v1.0.0 (2025-05-06 기준)
