"""Module docstring."""

import importlib.machinery
import importlib.util
import inspect
import os
import shutil
import sys
import types

# ✅ 프로젝트 루트 및 모듈 경로 설정
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_MODULES = os.path.join(PROJECT_ROOT, "modules")
if BASE_MODULES not in sys.path:
    sys.path.insert(0, BASE_MODULES)

# ✅ __pycache__ 정리
sys.path = [p for p in sys.path if "clean_rebuild" not in p]
for root, dirs, files in os.walk(BASE_MODULES):
    if "__pycache__" in dirs:
        shutil.rmtree(os.path.join(root, "__pycache__"))

# ✅ account_runner 모듈 임포트
import account_runner

spec = importlib.util.find_spec("account_runner")
print(f"📂 Loaded account_runner from: {spec.origin if spec else '❌ Not Found'}")

functions = [f for f, _ in inspect.getmembers(account_runner, inspect.isfunction)]
print(f"📜 Functions in account_runner: {functions}")

# ✅ logger 모듈 동적 로드
LOGGER_PATH = os.path.join(BASE_MODULES, "common", "logger.py")
loader = importlib.machinery.SourceFileLoader("logger", LOGGER_PATH)
logger = types.ModuleType("logger")
logger.__file__ = LOGGER_PATH
loader.exec_module(logger)

print(f"📂 Loaded logger from: {LOGGER_PATH}")
print(
    f"📜 insert_session_log signature: {inspect.signature(logger.insert_session_log)}"
)


def main():
    """Function `main` docstring."""
    import time

    session_id = "sess_" + time.strftime("%Y%m%d_%H%M%S")
    logger.init_db()
    logger.insert_session_log(
        session_id=session_id, status="START", message="🚀 계정 실행 시작"
    )
    account_runner.init_log_db()
    print("🚀 계정 실행 시작")

    import asyncio

    asyncio.run(account_runner.run_all_accounts(session_id))

    print("🏁 모든 계정 실행 완료")
    logger.insert_session_log(
        session_id=session_id, status="END", message="🏁 모든 계정 실행 완료"
    )


if __name__ == "__main__":
    main()
