import ast
import os

import astor

BASE_DIR = r"C:\SNS_24AutoProject_250723"
TARGET_DIRS = ["launcher", "modules", "tests"]
INSERTED_COUNT = 0


def insert_docstring(node, default_doc):
    global INSERTED_COUNT
    if not ast.get_docstring(node):
        doc_node = ast.Expr(value=ast.Str(default_doc))
        node.body.insert(0, doc_node)
        INSERTED_COUNT += 1


def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)

        insert_docstring(tree, "Module docstring.")
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                insert_docstring(node, f"Function `{node.name}` docstring.")
            elif isinstance(node, ast.AsyncFunctionDef):
                insert_docstring(node, f"Async function `{node.name}` docstring.")
            elif isinstance(node, ast.ClassDef):
                insert_docstring(node, f"Class `{node.name}` docstring.")

        updated_code = astor.to_source(tree)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_code)

    except Exception as e:
        print(f"[ERROR] {file_path}: {e}")


def run():
    for folder in TARGET_DIRS:
        abs_folder = os.path.join(BASE_DIR, folder)
        for root, _, files in os.walk(abs_folder):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    process_file(file_path)
    print(f"\n✅ Docstring 삽입 완료: {INSERTED_COUNT} 개 항목 수정됨")


if __name__ == "__main__":
    run()
