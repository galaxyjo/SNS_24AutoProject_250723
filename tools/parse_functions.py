
                    node, 'end_lineno') else node.body[-1].lineno
                code_lines = source.splitlines()[start_line:end_line]
                code_str = '\n'.join(code_lines)
                end_line = node.end_lineno if hasattr(
                full_path = os.path.join(dirpath, file)
                func_name = node.name
                functions.append((filepath, func_name, hash_val))
                hash_val = hash_function_code(code_str)
                result.extend(extract_functions_from_file(full_path))
                start_line = node.lineno - 1
            if file.endswith('.py'):
            if isinstance(node, ast.FunctionDef):
            source = f.read()
        for file in filenames:
        for node in ast.walk(tree):
        print(f"Error in {filepath}: {e}")
        tree = ast.parse(source)
        with open(filepath, 'r', encoding='utf-8') as f:
        writer = csv.writer(csvfile)
        writer.writerow(['파일명', '함수명', '해시값'])
        writer.writerows(data)
    all_functions = scan_directory(base_dir)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    except Exception as e:
    for dirpath, _, filenames in os.walk(root_dir):
    functions = []
    print(f"[완료] 함수 해시 추출 완료: {len(all_functions)}개 함수 → function_hash_map.csv 저장됨")
    result = []
    return functions
    return hashlib.sha256(code.encode('utf-8')).hexdigest()
    return result
    save_to_csv(all_functions)
    try:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
def extract_functions_from_file(filepath):
def hash_function_code(code):
def save_to_csv(data, output_file='function_hash_map.csv'):
def scan_directory(root_dir):
if __name__ == '__main__':
import ast
import csv
import hashlib
import os
