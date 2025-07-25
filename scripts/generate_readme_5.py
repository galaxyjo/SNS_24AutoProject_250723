
    f.write(content)
- `backup_YYYYMMDD.zip`: 전체 시스템 백업 파일
- `configs\\`: 설정 파일(JSON/CONF)
- `dashboards\\`: Streamlit 대시보드
- `db\\`: SQLite DB 저장 위치
- `insert_logtrace_auto.ps1`: 로그 자동 삽입 스크립트
- `logs\\`: 실행 및 시스템 로그
- `main.py`: 실행 메인 스크립트
- `modules\\`: 자동화 기능 모듈
- `scripts\\`: 보조 자동화 스크립트
- `session_log.db`: 세션 기반 추적 정보 저장
- `static\\`: 이미지 등 정적 자원
- `trace_log.db`: 함수 호출 로그 저장
"""
## 구성 디렉터리
## 로그 시스템
## 백업 파일
**생성 시각:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
content = f"""# 📘 SNS 24시간 자동화 시스템
filename = f"README_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
from datetime import datetime
import os
os.makedirs(output_path, exist_ok=True)
output_path = "docs"
print(f"✅ README 생성 완료: {filename}")
with open(os.path.join(output_path, filename), "w", encoding="utf-8") as f:
