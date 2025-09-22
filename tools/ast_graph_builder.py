# modules/tools/ast_graph_builder.py

import ast


def extract_functions(source_code):
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return []
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
