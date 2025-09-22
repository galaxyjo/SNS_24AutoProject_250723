import os
import re
import sys


def main(import_txt, project_root, out_txt):
    py_paths = []

    with open(import_txt, encoding="utf-8") as f:
        for line in f:
            # import 구문 추출 (from modules.x.y import z  / import modules.x)
            m = re.search(r"(?:from|import)\s+([\w\.]+)", line)
            if not m:
                continue
            mod = m.group(1).split(".")[0:3]  # modules.common.logger → 3레벨까지만
            rel_path = os.path.join(*mod) + ".py"  # modules\common\logger.py
            abs_path = os.path.join(project_root, rel_path)
            if os.path.isfile(abs_path):
                py_paths.append(abs_path)

    # 중복 제거 후 저장
    with open(out_txt, "w", encoding="utf-8") as f:
        for p in sorted(set(py_paths)):
            f.write(p + "\n")

    print(f"✅ needed_files.txt 생성: {len(py_paths)}개 파일")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "사용법: python needed_files_from_imports.py <import.txt> <project_root> <out.txt>"
        )
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
