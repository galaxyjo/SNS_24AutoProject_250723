# modules/core/main_features.py

import asyncio
import os

from modules import account_runner
from utils.env_loader import load_env

# 환경 변수 로딩
load_env()

BASE_PATH = os.getenv("BASE_PATH", "C:/SNS_24AutoProject_250723")
DB_PATH = os.getenv("DB_PATH", os.path.join(BASE_PATH, "db/trace_log.db"))


async def run_all(session_id: str = None) -> None:
    print(f"[CORE] main_features.run_all() 시작 (session_id={session_id})")
    await account_runner.run_all_accounts(session_id)
    print("[CORE] main_features.run_all() 완료")


def init_core() -> str:
    print("[CORE] 초기화 시작")
    print(f"[CORE] BASE_PATH={BASE_PATH}")
    print(f"[CORE] DB_PATH={DB_PATH}")
    return "core_init_ok"


# ✅ 테스트용 dummy 함수 추가 (mock patch용)
async def execute_account(session_id: str, account_id: str) -> str:
    """
    Dummy execute_account for test_account_runner.py mock target
    """
    return "ok"


if __name__ == "__main__":
    init_core()
    asyncio.run(run_all("manual_test_session"))
# modules/core/main_features.py


class RunFinishedError(Exception):
    """작업 완료 예외 (더미 예외)"""

    pass


def current_task():
    """현재 태스크 반환 더미 함수"""
    return None
