import ast
import csv
import hashlib
import os


def hash_function_code(code):
    return hashlib.sha256(code.encode("utf-8")).hexdigest()


def extract_functions_from_file(filepath):
    functions = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                start_line = node.lineno - 1
                end_line = (
                    node.end_lineno
                    if hasattr(node, "end_lineno")
                    else node.body[-1].lineno
                )
                code_lines = source.splitlines()[start_line:end_line]
                code_str = "\n".join(code_lines)
                hash_val = hash_function_code(code_str)
                functions.append((filepath, func_name, hash_val))
    except Exception as e:
        print(f"Error in {filepath}: {e}")
    return functions


def scan_directory(root_dir):
    result = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".py"):
                full_path = os.path.join(dirpath, file)
                result.extend(extract_functions_from_file(full_path))
    return result


def save_to_csv(data, output_file="function_hash_map.csv"):
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["파일명", "함수명", "해시값"])
        writer.writerows(data)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_functions = scan_directory(base_dir)
    save_to_csv(all_functions)
    print(
        f"[완료] 함수 해시 추출 완료: {len(all_functions)}개 함수 → function_hash_map.csv 저장됨"
    )
