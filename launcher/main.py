import sys
import os
import shutil
import importlib.util
import importlib.machinery
import inspect
import types

# ============================================
# 1️⃣ 프로젝트 루트 자동 탐지
# ============================================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_MODULES = os.path.join(PROJECT_ROOT, "modules")

# ✅ modules 경로 강제 추가 (중복 방지)
if BASE_MODULES not in sys.path:
    sys.path.insert(0, BASE_MODULES)

# sys.path에서 외부 clean_rebuild 제거
sys.path = [p for p in sys.path if "clean_rebuild" not in p]

# ============================================
# 2️⃣ __pycache__ 삭제
# ============================================
for root, dirs, files in os.walk(BASE_MODULES):
    if "__pycache__" in dirs:
        shutil.rmtree(os.path.join(root, "__pycache__"))

# ============================================
# 3️⃣ account_runner 정상 로드
# ============================================
spec = importlib.util.find_spec("account_runner")
print(f"📂 Loaded account_runner from: {spec.origin if spec else '❌ Not Found'}")

import account_runner
functions = [f for f, _ in inspect.getmembers(account_runner, inspect.isfunction)]
print(f"📜 Functions in account_runner: {functions}")

# ============================================
# 4️⃣ logger 절대경로 강제 로드
# ============================================
LOGGER_PATH = os.path.join(BASE_MODULES, "common", "logger.py")
loader = importlib.machinery.SourceFileLoader("logger", LOGGER_PATH)
logger = types.ModuleType("logger")
logger.__file__ = LOGGER_PATH
loader.exec_module(logger)

print(f"📂 Loaded logger from: {LOGGER_PATH}")
print(f"📜 insert_session_log signature: {inspect.signature(logger.insert_session_log)}")

# ============================================
# 5️⃣ 메인 실행 함수
# ============================================
def main():
    import time
    session_id = "sess_" + time.strftime("%Y%m%d_%H%M%S")

    logger.init_db()
    logger.insert_session_log(session_id=session_id, status="START", message="🚀 계정 실행 시작")

    account_runner.init_log_db()

    print("🚀 계정 실행 시작")
    import asyncio
    asyncio.run(account_runner.run_all_accounts(session_id))
    print("🏁 모든 계정 실행 완료")

    logger.insert_session_log(session_id=session_id, status="END", message="🏁 모든 계정 실행 완료")

# ============================================
# 6️⃣ 진입점
# ============================================
if __name__ == "__main__":
    main()
