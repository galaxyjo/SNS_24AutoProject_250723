import os
import json
from typing import Any
from dotenv import load_dotenv

# ✅ 환경 변수 로드
load_dotenv()

# ✅ BASE_PATH 설정
BASE_PATH = os.getenv("BASE_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# ✅ 유틸: 경로 검증
def ensure_path_exists(path: str) -> None:
    if not os.path.exists(path):
        print(f"⚠️ 경로 없음: {path}")
        raise FileNotFoundError(f"경로 없음: {path}")

# ✅ 유틸: 완료 목록에 파일명 기록
def save_completed_file(filename: str) -> None:
    completed_path = os.path.join(BASE_PATH, "A_manual_fixed_list.txt")
    with open(completed_path, "a", encoding="utf-8") as f:
        f.write(f"{filename}\n")

# ✅ 주요 로직 예시 함수
def parse_audit_json(file_path: str) -> dict[str, Any]:
    ensure_path_exists(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    extracted = {
        "issue_id": data.get("issueId"),
        "url": data.get("url"),
        "type": data.get("type"),
    }

    print("✅ JSON 파싱 완료")
    return extracted

# ✅ 수정된 export_result 함수 (회장님 지정 경로 고정)
def export_result(data: dict[str, Any], filename: str = "audit_result.xlsx") -> None:
    try:
        import pandas as pd
        from openpyxl import Workbook  # fallback

        export_dir = os.path.join(BASE_PATH, "data", "exported_data")
        os.makedirs(export_dir, exist_ok=True)

        df = pd.DataFrame([data])
        save_path = os.path.join(export_dir, filename)
        df.to_excel(save_path, index=False)
        print(f"✅ 결과 저장 완료: {save_path}")
    except ImportError:
        print("⚠️ openpyxl 미설치됨")

# ✅ main 진입점
def main() -> None:
    sample_path = os.path.join(BASE_PATH, "data", "sample_audit.json")

    try:
        result = parse_audit_json(sample_path)
        export_result(result)
        save_completed_file("audits_1.py")
    except Exception as e:
        print(f"⚠️ 처리 실패: {e}")

if __name__ == "__main__":
    main()
