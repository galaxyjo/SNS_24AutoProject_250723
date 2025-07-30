import os
import sqlite3
import asyncio
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db', 'account_log.db')

MAX_RETRIES = 3
CIRCUIT_BREAK_THRESHOLD = 2  # 실패 2회 이상이면 중단

def init_log_db():
    os.makedirs(os.path.join(BASE_DIR, 'db'), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account_run_log (
            session_id TEXT,
            account TEXT,
            status TEXT,
            message TEXT,
            run_at TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ account_run_log 테이블 확인 완료")
    print("📂 DB 경로 확인:", DB_PATH)

def get_run_at_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def log_account_run(session_id, account_name, status, message):
    run_at = get_run_at_timestamp()
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO account_run_log (session_id, account, status, message, run_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (session_id, account_name, status, message, run_at))
        conn.commit()
        conn.close()
        print(f"✅ 로그 저장됨: {account_name}, 상태: {status}, 시간: {run_at}")
    except Exception as e:
        print(f"❌ 로그 저장 실패: {account_name} → {e}")

async def run_account(session_id: str, account_name: str) -> bool:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"▶ 실행 중: {account_name} (시도 {attempt}/{MAX_RETRIES})")
            await asyncio.sleep(0.01)
            if account_name.startswith("account_02"):
                raise Exception("❌ 예외 발생: account_02 실패")
            log_account_run(session_id, account_name, "SUCCESS", "정상 처리 완료")
            return True
        except Exception as e:
            error_msg = f"❌ 예외 발생: {str(e)}"
            print(error_msg)
            if attempt == MAX_RETRIES:
                log_account_run(session_id, account_name, "FAIL", error_msg)
                return False
            await asyncio.sleep(0.05)
        finally:
            if attempt == MAX_RETRIES:
                print(f"📌 로그 기록 시도 완료: {account_name}")

async def run_all_accounts(session_id: str) -> None:
    # ✅ 실패 계정 2개 넣어 Circuit Breaker 발동 테스트
    account_list = ['account_01', 'account_02', 'account_02']
    failure_count = 0
    for acc in account_list:
        result = await run_account(session_id, acc)
        if not result:
            failure_count += 1
            if failure_count >= CIRCUIT_BREAK_THRESHOLD:
                print("🛑 Circuit Breaker 작동: 실패 횟수 초과 → 나머지 계정 실행 중단")
                break
