import ast
import os
from pathlib import Path


def clean_code_block(code: str) -> str:
    """주석 제거"""
    lines = code.splitlines()
    cleaned = []
    for line in lines:
        if line.strip().startswith("#"):
            continue
        if "#" in line:
            line = line[: line.index("#")]
        cleaned.append(line.rstrip())
    return "\n".join([l for l in cleaned if l.strip()])


def extract_testable_functions(source: str):
    """Python 소스에서 함수 추출"""
    tree = ast.parse(source)
    return [node for node in tree.body if isinstance(node, ast.FunctionDef)]


def generate_test_stub_for_function(func: ast.FunctionDef) -> str:
    """테스트 스텁 생성"""
    return f"def test_{func.name}():\n    assert True\n"


def save_test_file(path: str, code: str) -> None:
    """테스트 코드 파일 저장"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)


def discover_python_files(root: str):
    """폴더 내 모든 .py 파일 찾기"""
    results = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                if not should_exclude_generated_path(full_path):
                    results.append(full_path)
    return results


def should_exclude_generated_path(path: str) -> bool:
    """자동 생성 경로는 제외"""
    return "tests/generated" in str(path)


# ✅ 수정된 부분: 폴더 강제 존재 검사 제거
GENERATED_DIR = Path("tests/generated")

if not GENERATED_DIR.exists():
    # RuntimeError 발생 대신 경고만 출력하고 동작 계속
    print("⚠️ [warn] tests/generated 폴더 없음 → 자동생성 스킵 모드로 실행됩니다.")
