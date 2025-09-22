import os

# Docstring을 추가할 루트 디렉토리들
TARGET_DIRS = ["launcher", "modules", "core", "services"]

DOCSTRING_TEMPLATE = '''"""
{filename} Module
- 자동 생성된 Docstring
- TODO: 기능 설명 작성
"""
'''


def add_docstring_to_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 이미 Docstring이 있는 경우 스킵
    if content.strip().startswith('"""') or content.strip().startswith("'''"):
        return False

    filename = os.path.basename(file_path)
    docstring = DOCSTRING_TEMPLATE.format(filename=filename)
    new_content = docstring + "\n" + content

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    root = os.getcwd()
    updated_files = []
    for target_dir in TARGET_DIRS:
        dir_path = os.path.join(root, target_dir)
        for subdir, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(subdir, file)
                    if add_docstring_to_file(path):
                        updated_files.append(path)

    print("✅ Docstring 추가 완료:", len(updated_files), "files")
    for f in updated_files:
        print("   →", f)


if __name__ == "__main__":
    main()
