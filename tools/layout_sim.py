import argparse
import json
import os


def validate_paths(plan):
    missing = []
    for item in plan:
        src = item["file"]
        dst = os.path.join("C:\\clean_rebuild_final", item["target_dir"])

        if not os.path.exists(src):
            print(f"[❌] 원본 없음: {src}")
            missing.append(f"[❌] 원본 없음: {src}")
        if not os.path.exists(dst):
            print(f"[ℹ️] 대상 폴더 없음 → 생성 예정: {dst}")
        print(f"[🔄] 이동 예정: {src} → {dst}")
    return missing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    parser.add_argument("--whatif", action="store_true")
    args = parser.parse_args()

    with open(args.plan, encoding="utf-8") as f:
        plan = json.load(f)

    print(f"\n[✓] 총 {len(plan)}개 파일 이동 시뮬레이션 시작\n")

    errors = validate_paths(plan)

    if errors:
        print("\n[⚠️] 다음 파일은 존재하지 않음:")
        for err in errors:
            print("    ", err)
    else:
        print("\n[✅] 모든 경로 유효. 실제 이동 가능.")


if __name__ == "__main__":
    main()
