# tools/analyze_missing_usage.py
import argparse
import ast
import csv
import os


def extract_imports_from_file(filepath):
    imports = set()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            node = ast.parse(f.read(), filename=filepath)
        for n in ast.walk(node):
            if isinstance(n, ast.Import):
                for alias in n.names:
                    imports.add(alias.name.split(".")[0])
            elif isinstance(n, ast.ImportFrom):
                if n.module:
                    imports.add(n.module.split(".")[0])
    except Exception:
        pass
    return imports


def build_dependency_map(source_root):
    dep_map = {}
    for root, _, files in os.walk(source_root):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, source_root).replace("\\", "/")
                imports = extract_imports_from_file(full_path)
                dep_map[rel_path] = imports
    return dep_map


def resolve_used_modules(entrypoint, dep_map):
    used = set()
    to_check = [entrypoint.replace("\\", "/")]

    while to_check:
        current = to_check.pop()
        if current in used:
            continue
        used.add(current)
        imported = dep_map.get(current, set())
        for imp in imported:
            for mod_path in dep_map:
                if mod_path.startswith(imp) or f"/{imp}.py" in mod_path:
                    if mod_path not in used:
                        to_check.append(mod_path)
    return used


def load_missing_filenames(csv_path):
    with open(csv_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row["filename"].replace("\\", "/") for row in reader]


def write_analysis_result(output_path, missing_files, used_files):
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "used_in_main_chain", "used_by"])
        for mf in missing_files:
            used = "✅" if mf in used_files else "❌"
            writer.writerow([mf, used, "main_chain" if used == "✅" else ""])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--missing_csv", required=True)
    parser.add_argument("--entrypoint", required=True)
    parser.add_argument("--source_root", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    dep_map = build_dependency_map(args.source_root)
    used = resolve_used_modules(args.entrypoint, dep_map)
    missing = load_missing_filenames(args.missing_csv)
    write_analysis_result(args.output, missing, used)


if __name__ == "__main__":
    main()
