# verify_integrity_and_identify_unnecessary.py
import hashlib
import json
import os


def calculate_sha256(file_path):
    h = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except BaseException:
        return None


def main():
    root = input("📂 프로젝트 루트 경로 입력: ").strip()
    if not os.path.isdir(root):
        print("❌ 오류: 잘못된 경로")
        return

    baseline = input("📄 기준 해시 파일 경로 입력 (master_hashes.json): ").strip()
    if not os.path.isfile(baseline):
        print("❌ 오류: 기준 해시 파일 없음")
        return

    with open(baseline, "r", encoding="utf-8") as f:
        reference = json.load(f)

    current = {}
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            file_path = os.path.join(dirpath, f)
            rel_path = os.path.relpath(file_path, root)
            current[rel_path] = calculate_sha256(file_path)

    changed, new_files, deleted = [], [], []

    for rel, h in current.items():
        if rel in reference:
            if h != reference[rel]:
                changed.append(rel)
        else:
            new_files.append(rel)

    for rel in reference.keys():
        if rel not in current:
            deleted.append(rel)

    print("\n✅ 검증 결과")
    print(f"총 파일: {len(current)}")
    if changed:
        print("\n❗ 변경된 파일:")
        for c in changed:
            print("-", c)
    if new_files:
        print("\n📄 신규 파일:")
        for n in new_files:
            print("-", n)
    if deleted:
        print("\n🗑️ 삭제된 파일:")
        for d in deleted:
            print("-", d)
    if not changed and not new_files and not deleted:
        print("모든 파일이 기준과 일치합니다.")


if __name__ == "__main__":
    main()
