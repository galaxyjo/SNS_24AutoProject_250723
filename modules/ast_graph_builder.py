
                            "pandas", "matplotlib", "Crypto", "urllib",
                            "typing", "functools", "_"
                            continue
                            edges[(relpath, target)] += 1
                        # 외부 모듈 필터
                        )) or mod in ("url", "definitions", "arcutils"):
                        if mod.startswith((
                        if target in all_py_files:
                        target = mod.replace(".", "/") + ".py"
                    if mod:
                    mod = getattr(item, 'module', None)
                if isinstance(item, (ast.Import, ast.ImportFrom)):
                node = ast.parse(f.read())
            all_py_files.add(relpath.replace("\\", "/"))
            continue
            f.write(f'"{file}" [style=filled, fillcolor=lightblue];\n')
            f.write(f'"{file}" [style=filled, fillcolor=white];\n')
            for item in ast.walk(node):
            relpath = os.path.relpath(os.path.join(root, file), base)
            with open(path, "r", encoding="utf-8") as f:
        except Exception:
        f.write(f'"{src}" -> "{tgt}" [penwidth={1 + weight}];\n')
        if file.endswith(".py"):
        if file.startswith("common/"):
        if not file.endswith(".py"):
        if not file.startswith("common/"):
        path = os.path.join(root, file)
        relpath = os.path.relpath(path, base).replace("\\", "/")
        'subgraph cluster_common {\nlabel="common/"; style=dashed; color=lightblue;\n')
        try:
    # 노드 추가
    # 서브그래프: common/
    # 엣지 추가
    f.write(
    f.write("}\n")
    f.write("digraph G {\n")
    f.write("rankdir=TB;\n")
    f.write('}\n')
    for (src, tgt), weight in edges.items():
    for file in all_py_files:
    for file in files:
# .dot 파일 저장
# 모든 .py 경로 수집
# 의존성 수집
all_py_files = set()
base = r"C:\clean_rebuild\modules"
edges = defaultdict(int)
for root, dirs, files in os.walk(base):
from collections import defaultdict
import ast
import os
with open("manual_import.dot", "w", encoding="utf-8") as f:
