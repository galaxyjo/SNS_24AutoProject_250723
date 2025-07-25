import os
import sqlite3
import asyncio
from datetime import datetime

# ✅ 절대경로 기반 DB 경로 고정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db', 'account_log.db')

# ✅ DB 및 테이블 자동 생성
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

# ✅ 타임스탬프 생성
def get_run_at_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ✅ 로그 저장
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

# ✅ 단일 계정 실행 (비동기)
async def run_account(session_id: str, account_name: str) -> None:
    try:
        print(f"▶ 실행 중: {account_name}")
        await asyncio.sleep(0.01)
        if account_name == "account_02":
            raise Exception("❌ 예외 발생: account_02 실패")
        log_account_run(session_id, account_name, "SUCCESS", "정상 처리 완료")
    except Exception as e:
        error_msg = f"❌ 예외 발생: {str(e)}"
        print(error_msg)
        log_account_run(session_id, account_name, "FAIL", error_msg)
    finally:
        print(f"📌 로그 기록 시도 완료: {account_name}")

# ✅ 전체 계정 병렬 실행
async def run_all_accounts(session_id: str) -> None:
    account_list = ['account_01', 'account_02', 'account_03']
    tasks = [run_account(session_id, acc) for acc in account_list]
    await asyncio.gather(*tasks)
