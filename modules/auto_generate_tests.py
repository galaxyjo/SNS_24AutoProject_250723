
            f.write(generate_test_stub(fn))
        # 기본 대상 지정 — 필요 시 수정
        auto_generate_tests("account_runner.py", "test_account_runner.py")
        auto_generate_tests(target, out)
        f.write(f"import pytest\nfrom {module_name} import *\n")
        for fn in funcs:
        node = ast.parse(f.read())
        out = sys.argv[2] if len(sys.argv) >= 3 else f"test_{Path(target).stem}.py"
        target = sys.argv[1]
    # ('example_input', 'expected_output'),
    assert {func_name}(inp) == expected
    else:
    funcs = extract_functions(target_py)
    if len(sys.argv) >= 2:
    module_name = Path(target_py).stem  # 파일명 → 모듈명
    print(f"✅  {output_test_py} 생성 — 함수 {len(funcs)}개 스텁 완료")
    return [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
    return f"""
    with open(file_path, "r", encoding="utf-8-sig") as f:
    with open(output_test_py, "w", encoding="utf-8") as f:
"""
# ------------------------------------------------------------------
#    예) python auto_generate_tests.py myfile.py mytests.py
# 1) 대상 .py 파일에서 함수명 추출 (BOM 안전 ― utf-8-sig)
# 2) 함수 하나당 pytest 템플릿 생성
# 3) 테스트 파일 자동 생성
# 4) 직접 실행 시: CLI 인자 우선, 없으면 기본값
@pytest.mark.parametrize('inp, expected', [
])
def auto_generate_tests(target_py: str, output_test_py: str):
def extract_functions(file_path: str):
def generate_test_stub(func_name: str) -> str:
def test_{func_name}(inp, expected):
from pathlib import Path
if __name__ == "__main__":
import ast
import sys
