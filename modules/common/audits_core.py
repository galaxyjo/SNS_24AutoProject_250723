# modules/common/audits_core.py
# 🚀 통합 스크립트
# 출처: audits_1.py (dict_helper 제외)
# 기능: 감사 데이터(JSON) 파싱 및 결과 Export

import os
import json
from typing import Any
from dotenv import load_dotenv

# ✅ 환경 변수 로드
load_dotenv()

# ✅ BASE_PATH 설정
BASE_PATH = os.getenv("BASE_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


def ensure_path_exists(path: str) -> None:
    """경로 유효성 검증"""
    if not os.path.exists(path):
        print(f"⚠️ 경로 없음: {path}")
        raise FileNotFoundError(f"경로 없음: {path}")


def save_completed_file(filename: str) -> None:
    """수정 완료된 파일명을 로그로 기록"""
    completed_path = os.path.join(BASE_PATH, "A_manual_fixed_list.txt")
    with open(completed_path, "a", encoding="utf-8") as f:
        f.write(f"{filename}\n")


def parse_audit_json(file_path: str) -> dict[str, Any]:
    """Audit JSON 파일 파싱"""
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


def export_result(data: dict[str, Any], filename: str = "audit_result.xlsx") -> None:
    """감사 결과를 Excel로 내보내기"""
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


def main() -> None:
    """샘플 실행 엔트리포인트"""
    sample_path = os.path.join(BASE_PATH, "data", "sample_audit.json")

    try:
        result = parse_audit_json(sample_path)
        export_result(result)
        save_completed_file("audits_core.py")
    except Exception as e:
        print(f"⚠️ 처리 실패: {e}")


if __name__ == "__main__":
    main()
