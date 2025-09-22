import os
import sys


def load_filenames_from_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return set(os.path.basename(line.strip()) for line in f if line.strip())


def scan_py_files(root):
    matched = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(".py"):
                matched.append(os.path.join(dirpath, fname))
    return matched


def main(list_main, scan_root, out_path):
    # 1. 기준 파일명 목록 불러오기
    target_filenames = load_filenames_from_txt(list_main)

    # 2. 전체 .py 파일 스캔
    found_files = scan_py_files(scan_root)

    # 3. 파일명으로 교집합 필터링
    matched = [f for f in found_files if os.path.basename(f) in target_filenames]

    # 4. 결과 저장
    with open(out_path, "w", encoding="utf-8") as f:
        for path in matched:
            f.write(f"{path}\n")

    print(f"✅ needed_files.txt 생성 완료: {len(matched)}개 파일")


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(
            "사용법: needed_files_by_name.py --list-main <file> --scan-root <dir> --out <output>"
        )
        sys.exit(1)
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    main(args["--list-main"], args["--scan-root"], args["--out"])
