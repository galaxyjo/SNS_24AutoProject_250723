
            missing.append(f"[❌] 원본 없음: {src}")
            print("    ", err)
            print(f"[ℹ️] 대상 폴더 없음 → 생성 예정: {dst}")
        dst = os.path.join("C:\\clean_rebuild_final", item["target_dir"])
        for err in errors:
        if not os.path.exists(dst):
        if not os.path.exists(src):
        plan = json.load(f)
        print("\n[✅] 모든 경로 유효. 실제 이동 가능.")
        print("\n[⚠️] 다음 파일은 존재하지 않음:")
        print(f"[🔄] 이동 예정: {src} → {dst}")
        src = item["file"]
    args = parser.parse_args()
    else:
    errors = validate_paths(plan)
    for item in plan:
    if errors:
    main()
    missing = []
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    parser.add_argument("--whatif", action="store_true")
    print(f"\n[✓] 총 {len(plan)}개 파일 이동 시뮬레이션 시작\n")
    return missing
    with open(args.plan, encoding='utf-8') as f:
def main():
def validate_paths(plan):
if __name__ == "__main__":
import argparse
import json
import os
