import os
from collections import defaultdict
from typing import DefaultDict, Set


def collect_py_files(base_dir: str) -> Set[str]:
    all_py_files: Set[str] = set()
    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".py"):
                continue
            path = os.path.join(root, file)
            relpath = os.path.relpath(path, base_dir).replace("\\", "/")
            all_py_files.add(relpath)
    return all_py_files


def write_dot_file(py_files: Set[str], output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("digraph G {\n")
        f.write("rankdir=TB;\n")
        for file in py_files:
            f.write(f'"{file}" [style=filled, fillcolor=white];\n')
        f.write("}\n")


def build_dependency_graph(base_dir: str, output_path: str) -> None:
    py_files = collect_py_files(base_dir)
    write_dot_file(py_files, output_path)


if __name__ == "__main__":
    BASE_DIR = "C:/clean_rebuild/modules"
    OUTPUT_FILE = "manual_import.dot"
    build_dependency_graph(BASE_DIR, OUTPUT_FILE)
