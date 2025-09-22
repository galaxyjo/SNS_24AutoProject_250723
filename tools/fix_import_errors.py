# tools/fix_import_errors.py

import ast
import os

# 📌 모듈 경로 설정
MODULES_DIR = os.path.join("modules")
GENERATED_TESTS_DIR = os.path.join("tests", "generated")


def extract_imports_from_test(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith("modules."):
                for alias in node.names:
                    imports.append((node.module.replace("modules.", ""), alias.name))
    return imports


def check_function_exists(module_name, func_name):
    module_path = os.path.join(MODULES_DIR, f"{module_name}.py")
    if not os.path.exists(module_path):
        return False, "❌ 파일 없음"
    with open(module_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return True, "✅ 함수 존재"
    return False, "❌ 함수 없음"


def main():
    print(f"📂 진단 시작: {GENERATED_TESTS_DIR}\n")
    for filename in os.listdir(GENERATED_TESTS_DIR):
        if filename.endswith(".py"):
            path = os.path.join(GENERATED_TESTS_DIR, filename)
            print(f"📄 테스트 파일: {filename}")
            imports = extract_imports_from_test(path)
            if not imports:
                print("  ⚠️  모듈 import 없음\n")
                continue
            for module, func in imports:
                exists, msg = check_function_exists(module, func)
                print(f"   - 🔍 modules/{module}.py → '{func}': {msg}")
            print()


if __name__ == "__main__":
    main()
