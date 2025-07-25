
---
    "w",
    encoding="utf-8",
    f"docs/operational_plan_{datetime.now().strftime('%Y%m%d')}.md",
    f.write(content)
- admin 계정만 Export 및 외부연동 기능 허용
- Export 버튼: admin 계정만 표시
- Git 연동 로그 점검: git_log_insert.py
- login_and_permissions.py → session_id 기반 인증
- Streamlit 실행: dashboards\\dashboard_full_tabs.py
- user_credentials.db + session_log.db 기록 추적
- viewer 계정은 로그 조회만 가능
- Webhook 전송: send_log_webhook.py, auto_send_gitlog_webhook.py
- 로그 테이블 + 통계 시각화
- 백업 스크립트: scripts\\final_backup_YYYYMMDD.ps1
- 복원: 압축 해제 후 동일 경로 복사
- 응답코드 200 = 정상 전송
"""
# scripts/generate_operational_plan.py
## 1. 관리자 권한 정책
## 2. 백업 및 복원 시나리오
## 3. 세션 기반 보안 관리
## 4. 로그 대시보드 운영
## 5. 외부 연동 모니터링
) as f:
✅ 전체 시스템은 24시간 자동화 구성 상태입니다.
content = f"""# 🛠 운영 가이드 (Operational Plan)
from datetime import datetime
import os
os.makedirs("docs", exist_ok=True)
print("✅ 운영 가이드 생성 완료")
with open(
📁 프로젝트 경로: C:\\SNS_24AutoProject
📅 생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
