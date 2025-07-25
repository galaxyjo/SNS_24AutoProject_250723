
                matched.append(os.path.join(dirpath, fname))
            f.write(f"{path}\n")
            if fname.endswith('.py'):
        for fname in filenames:
        for path in matched:
        print("사용법: needed_files_by_name.py --list-main <file> --scan-root <dir> --out <output>")
        return set(os.path.basename(line.strip()) for line in f if line.strip())
        sys.exit(1)
    # 1. 기준 파일명 목록 불러오기
    # 2. 전체 .py 파일 스캔
    # 3. 파일명으로 교집합 필터링
    # 4. 결과 저장
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    for dirpath, _, filenames in os.walk(root):
    found_files = scan_py_files(scan_root)
    if len(sys.argv) != 7:
    main(args["--list-main"], args["--scan-root"], args["--out"])
    matched = []
    matched = [f for f in found_files if os.path.basename(f) in target_filenames]
    print(f"✅ needed_files.txt 생성 완료: {len(matched)}개 파일")
    return matched
    target_filenames = load_filenames_from_txt(list_main)
    with open(out_path, 'w', encoding='utf-8') as f:
    with open(path, 'r', encoding='utf-8') as f:
def load_filenames_from_txt(path):
def main(list_main, scan_root, out_path):
def scan_py_files(root):
if __name__ == "__main__":
import os
import sys
