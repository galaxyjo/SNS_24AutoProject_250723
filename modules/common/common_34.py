# modules/common/common_34.py (정밀 디버깅 후 전체 스크립트)

import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def load_json_file(path: str) -> dict:
    """지정된 경로의 JSON 파일을 읽어 dict 반환"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"파일이 존재하지 않습니다: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(data: dict, path: str) -> None:
    """dict 데이터를 지정된 경로의 JSON 파일로 저장"""
    folder = os.path.dirname(path)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    """테스트용 main 함수"""
    test_path = os.path.join(os.path.dirname(__file__), "test.json")
    sample_data = {"key": "value"}
    save_json_file(sample_data, test_path)
    loaded = load_json_file(test_path)
    print("✅ JSON 파일 읽기/쓰기 확인:", loaded)

if __name__ == "__main__":
    main()
