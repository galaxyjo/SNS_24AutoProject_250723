
                continue
                py_paths.append(abs_path)
            # import 구문 추출 (from modules.x.y import z  / import modules.x)
            abs_path = os.path.join(project_root, rel_path)
            f.write(p + '\n')
            if not m:
            if os.path.isfile(abs_path):
            m = re.search(r'(?:from|import)\s+([\w\.]+)', line)
            mod = m.group(1).split('.')[0:3]          # modules.common.logger → 3레벨까지만
            rel_path = os.path.join(*mod) + '.py'     # modules\common\logger.py
        for line in f:
        for p in sorted(set(py_paths)):
        print("사용법: python needed_files_from_imports.py <import.txt> <project_root> <out.txt>")
        sys.exit(1)
    # 중복 제거 후 저장
    if len(sys.argv) != 4:
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    print(f"✅ needed_files.txt 생성: {len(py_paths)}개 파일")
    py_paths = []
    with open(import_txt, encoding='utf-8') as f:
    with open(out_txt, 'w', encoding='utf-8') as f:
# 저장: C:\clean_rebuild\tools\needed_files_from_imports.py
def main(import_txt, project_root, out_txt):
if __name__ == "__main__":
import os
import re
import sys
