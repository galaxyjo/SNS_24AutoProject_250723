# modules/account_runner.py

import os
import sqlite3
import asyncio
import traceback
from datetime import datetime
import modules.core.main_features as core_main  # ✅ 간접 import로 변경 (patch 대상과 일치)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db', 'account_log.db')
MAX_RETRIES = 3
CIRCUIT_BREAK_THRESHOLD = 2


def init_log_db():
    os.makedirs(os.path.join(BASE_DIR, 'db'), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS account_run_log (
            session_id TEXT,
            account TEXT,
            status TEXT,
            message TEXT,
            run_at TEXT
        )
        """
    )
    conn.commit()
    conn.close()
    print('✅ account_run_log 테이블 확인 완료')
    print('📂 DB 경로 확인:', DB_PATH)


def get_run_at_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def log_account_run(session_id, account_name, status, message, conn=None):
    run_at = get_run_at_timestamp()
    own_conn = False

    try:
        if conn is None:
            conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            own_conn = True

        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS account_run_log (
                session_id TEXT,
                account TEXT,
                status TEXT,
                message TEXT,
                run_at TEXT
            )
            """
        )
        cursor.execute(
            "INSERT INTO account_run_log (session_id, account, status, message, run_at) VALUES (?, ?, ?, ?, ?)",
            (session_id, account_name, status, message, run_at)
        )
        conn.commit()
        print(f'✅ 로그 저장됨: {account_name}, 상태: {status}, 시간: {run_at}')
    except Exception as e:
        print(f'❌ 로그 저장 실패: {account_name} → {e}')
    finally:
        if own_conn:
            conn.close()


async def run_account(session_id: str, account_name: str) -> dict:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f'▶ 실행 중: {account_name} (시도 {attempt}/{MAX_RETRIES})')

            result = await core_main.execute_account(session_id, account_name)

            log_account_run(session_id, account_name, 'SUCCESS', '정상 처리 완료')
            return {
                "session_id": session_id,
                "account": account_name,
                "status": "success",
                "message": "정상 처리 완료"
            }

        except Exception as e:
            tb = traceback.format_exc()
            error_msg = f'❌ 예외 발생: {str(e)}\n{tb}'
            print(error_msg)
            if attempt == MAX_RETRIES:
                log_account_run(session_id, account_name, 'FAIL', str(e))
                return {
                    "session_id": session_id,
                    "account": account_name,
                    "status": "fail",
                    "message": str(e)
                }
            await asyncio.sleep(0.05)
        finally:
            if attempt == MAX_RETRIES:
                print(f'📌 로그 기록 시도 완료: {account_name}')


async def run_all_accounts(session_id: str) -> dict:
    account_list = ['account_01', 'account_02', 'account_02']
    failure_count = 0
    results = {}

    for acc in account_list:
        result = await run_account(session_id, acc)
        results[acc] = result

        if result["status"] != "success":
            failure_count += 1
            if failure_count >= CIRCUIT_BREAK_THRESHOLD:
                print('🛑 Circuit Breaker 작동: 실패 횟수 초과 → 나머지 계정 실행 중단')
                break

    return results
