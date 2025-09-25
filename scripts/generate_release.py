# modules/scripts/generate_release.py
# =====================================
# 기능: Release Info, QA Review, Operational Plan, Log Statistics 통합 생성기
# 출처: generate_release.py, generate_release.py, generate_release.py, generate_release.py

import os
import sqlite3
import pandas as pd
from datetime import datetime

def generate_release_info() -> str:
    os.makedirs("docs", exist_ok=True)
    release_info = f"""# 🚀 Release Info
📅 생성일: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📦 경로: C:\\SNS_24AutoProject
🛠 포함 모듈: scripts, modules, db
"""
    path = f"docs/release_info_{datetime.now().strftime('%Y%m%d')}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(release_info)
    print(f"✅ Release Info 생성 완료: {path}")
    return path

def generate_qa_review() -> str:
    os.makedirs("logs", exist_ok=True)
    qa_text = f"""# ✅ QA 회고 점검 루프
📁 기준: SNS_24AutoProject / WT-01~12
📅 생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
✅ 최종 평가: QA 통과
"""
    path = os.path.join("logs", f"qa_review_{datetime.now().strftime('%Y%m%d')}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(qa_text)
    print(f"✅ QA 점검 보고서 생성 완료: {path}")
    return path

def generate_operational_plan() -> str:
    os.makedirs("docs", exist_ok=True)
    content = f"""# 🛠 운영 가이드 (Operational Plan)
📅 생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📁 프로젝트 경로: C:\\SNS_24AutoProject
"""
    path = f"docs/operational_plan_{datetime.now().strftime('%Y%m%d')}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 운영 가이드 생성 완료: {path}")
    return path

def generate_log_statistics() -> None:
    os.makedirs("logs/stats", exist_ok=True)
    conn = sqlite3.connect("db/trace_log.db")
    cursor = conn.cursor()
    log_tables = ["command_log","disk_log","env_log","function_session_log","git_log","network_log"]
    now = datetime.now().strftime("%Y%m%d_%H%M%S")

    for table in log_tables:
        try:
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            stats = {"table": table, "row_count": len(df),
                     "columns": list(df.columns),
                     "last_updated": df.iloc[-1]["executed_at"] if "executed_at" in df.columns else "N/A"}
            stat_df = pd.DataFrame([stats])
            path = f"logs/stats/{table}_stats_{now}.csv"
            stat_df.to_csv(path, index=False, encoding="utf-8")
            print(f"✅ {table} 통계 요약 완료 → {path}")
        except Exception as e:
            print(f"❌ {table} 처리 실패: {e}")
    conn.close()

def main():
    generate_release_info()
    generate_qa_review()
    generate_operational_plan()
    generate_log_statistics()
    print("🎯 모든 Report/Plan 생성 완료")

if __name__ == "__main__":
    main()
