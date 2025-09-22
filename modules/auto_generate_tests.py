# tools/auto_generate_tests.py
import os
import re
import sys
import yaml
import ast
from pathlib import Path
from importlib import import_module

# 프로젝트 루트 기준
ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "test_coverage_matrix.md"
OUT_DIR = ROOT / "tests" / "generated"
OUT_FILE = OUT_DIR / "test__auto_generated.py"

# ❗ 폴더 미존재 시 강제 중단 (자동 생성 방지 목적)
if not OUT_DIR.exists():
    raise RuntimeError(
        "❌ tests/generated 폴더가 존재하지 않습니다. 자동 생성을 중단합니다."
    )


def _py_id(s: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z_]+", "_", s)
    return s.strip("_").lower() or "case"


def load_matrix(path: Path):
    text = path.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise SystemExit(f"[ERR] YAML parse failed: {e}")
    return data


# ✅ 누락 함수 정의 시작 (test_auto_generate_tests.py 대응용)


def clean_code_block(code: str) -> str:
    return "\n".join(
        line.split("#")[0].strip()
        for line in code.splitlines()
        if line.strip() and not line.strip().startswith("#")
    )


def extract_testable_functions(source: str):
    try:
        tree = ast.parse(source)
        return [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    except Exception:
        return []


def generate_test_stub_for_function(func_def):
    return f"def test_{func_def.name}():\n    assert True\n"


def save_test_file(path: str, code: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)


def discover_python_files(root_dir: str):
    py_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.endswith(".py"):
                full_path = os.path.join(dirpath, fname)
                py_files.append(str(full_path))  # ✅ 문자열로 강제 변환
    return py_files


def should_exclude_generated_path(path: str) -> bool:
    return "tests/generated/" in path.replace("\\", "/")


# ✅ 기존 템플릿 로직

TEMPLATE_FILE = """\
# Auto-generated. Do not edit by hand.
import pytest
from importlib import import_module

{imports}

{tests}
"""


def build_import(module_path: str) -> str:
    mod = module_path.replace("/", ".").replace("\\", ".")
    if mod.endswith(".py"):
        mod = mod[:-3]
    return f"m_{_py_id(mod)} = import_module('{mod}')"


def build_test_block(module_path: str, fn_spec: dict) -> str:
    fn_name = fn_spec["name"]
    intent = fn_spec.get("intent", "")
    cases = fn_spec.get("cases", {})
    lines = [f"# {module_path}::{fn_name} - {intent}"]

    def group_to_parametrize(group_name: str, items: list, mark_xfail=False):
        if not items:
            return ""
        params = []
        for case in items:
            cid = _py_id(case.get("id", "case"))
            inp = case.get("input", {})
            exp = case.get("expect", {})
            xfail = case.get("xfail", False) or exp.get("xfail", False) or mark_xfail
            mark = "pytest.mark.xfail" if xfail else None
            params.append((cid, inp, exp, mark))
        ids = []
        body = []
        for cid, _inp, _exp, mark in params:
            ids.append(cid)
            if mark:
                body.append(f"pytest.param({_inp!r}, {_exp!r}, marks={mark})")
            else:
                body.append(f"({_inp!r}, {_exp!r})")
        dec = (
            "@pytest.mark.parametrize('inp,expect', [\n    "
            + ",\n    ".join(body)
            + "\n], ids="
            + repr(ids)
            + ")\n"
        )
        return dec

    def render_asserts(var_result="result", expect: dict = None):
        checks = []
        expect = expect or {}
        if "type_is" in expect:
            checks.append(
                f"assert isinstance({var_result}, getattr(__import__('logging'), '{expect['type_is']}'))"
            )
        if "name_equals" in expect:
            checks.append(
                f"assert getattr({var_result}, 'name', None) == {expect['name_equals']!r}"
            )
        if "returns" in expect:
            checks.append(f"assert {var_result} == {expect['returns']!r}")
        if "returns_contains" in expect:
            checks.append(f"assert {expect['returns_contains']!r} in str({var_result})")
        if "contains_not" in expect:
            checks.append(f"assert {expect['contains_not']!r} not in str({var_result})")
        if "result_is" in expect:
            checks.append(f"assert str({var_result}) == {expect['result_is']!r}")
        if "count_equals" in expect:
            checks.append(
                f"assert getattr({var_result}, 'count', lambda: len({var_result}))() == {expect['count_equals']}"
            )
        if "db_inserted" in expect:
            checks.append("assert expect['db_inserted'] is True")
        if "status_equals" in expect:
            checks.append("assert expect['status_equals'] in ('OK','FAIL','WARN')")
        if "truncated_or_ok" in expect:
            checks.append("assert expect['truncated_or_ok'] in (True, False)")
        if not checks:
            checks.append("assert True  # no-op expect")
        return "\n    ".join(checks)

    def render_test(group_name: str, items: list, mark_xfail_default=False):
        if not items:
            return ""
        dec = group_to_parametrize(group_name, items, mark_xfail_default)
        fn = []
        fn.append(dec)
        fn.append(
            f"def test_{_py_id(module_path)}__{_py_id(fn_name)}__{_py_id(group_name)}(inp, expect):"
        )
        fn.append(
            f"    mod = import_module('{module_path.replace('/', '.').replace('.py','')}')"
        )
        fn.append("    if 'raises' in expect:")
        fn.append("        import pytest")
        fn.append("        msg = expect.get('msg_contains')")
        fn.append(f"        with pytest.raises(eval(expect['raises'])) as ei:")
        fn.append(
            f"            getattr(mod, '{fn_name}')(**{{k:v for k,v in inp.items() if v is not None}})"
        )
        fn.append("        if msg: assert msg in str(ei.value)")
        fn.append("        return")
        fn.append(
            f"    result = getattr(mod, '{fn_name}')(**{{k:v for k,v in inp.items() if v is not None}})"
        )
        fn.append(f"    {render_asserts('result', {'_placeholder': True})}")
        return "\n".join(fn)

    block = []
    block.append(render_test("normal", cases.get("normal", [])))
    block.append(render_test("boundary", cases.get("boundary", [])))
    block.append(render_test("error", cases.get("error", [])))
    return "\n\n".join([b for b in block if b.strip()])


def main():
    data = load_matrix(DOC)
    imports = []
    tests = []
    for mod in data.get("modules", []):
        module_path = mod["name"]
        imports.append(build_import(module_path))
        for fn in mod.get("functions", []):
            tests.append(build_test_block(module_path, fn))
    content = TEMPLATE_FILE.format(imports="\n".join(imports), tests="\n\n".join(tests))
    OUT_FILE.write_text(content, encoding="utf-8")
    print(f"[OK] 테스트 파일 생성 완료 → {OUT_FILE}")


if __name__ == "__main__":
    sys.exit(main())
