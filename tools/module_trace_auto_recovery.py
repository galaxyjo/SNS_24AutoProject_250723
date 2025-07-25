
# 1. 해시 파일 로드
# 2. main.py import 구문 파싱 (또는 수동 지정 리스트 사용)
# 3. 모듈명 → 해시 기반 매핑
# 4. 누락 모듈 추출 및 복구 대상 결정
# 5. 복구할 경우 파일 복사 수행
# 6. 결과 로그 저장 (리포트용)
copy_matched_files()
detect_missing_modules()
extract_main_imports()
import copy_matched_files
import detect_missing_modules
import extract_main_imports
import load_master_hash
import match_module_by_hash
import save_trace_report
load_master_hash()
match_module_by_hash()
save_trace_report("logs/module_trace_자동생성.csv")
