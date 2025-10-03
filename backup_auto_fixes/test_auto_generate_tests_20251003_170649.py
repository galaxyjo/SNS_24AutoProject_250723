# 📄 경로: tests/test_auto_generate_tests.py
import modules.auto_generate_tests as auto_generate_tests
from pathlib import Path
import os  # ⬅️ 추가됨


# ⛏️ RuntimeError 방지용 수정
def setup_module(module):
    os.makedirs("tests/generated", exist_ok=True)


def test_clean_code_block_removes_comments():
    code = "# comment\nx = 1  # inline"
    expected = "x = 1"
    result = auto_generate_tests.clean_code_block(code)
    assert result == expected


def test_extract_testable_functions_basic():
    source = "def foo():\n    return 1\ndef bar():\n    return 2"
    result = auto_generate_tests.extract_testable_functions(source)
    func_names = [f.name for f in result]
    assert "foo" in func_names
    assert "bar" in func_names


def test_generate_test_stub_for_function_contains_function_name():
    source = "def foo():\n    return 1"
    funcs = auto_generate_tests.extract_testable_functions(source)
    stub = auto_generate_tests.generate_test_stub_for_function(funcs[0])
    assert "def test_foo()" in stub


def test_save_test_file_creates_file(tmp_path):
    path = tmp_path / "test_sample.py"
    code = "def test_example():\n    assert True"
    auto_generate_tests.save_test_file(str(path), code)
    assert path.exists()
    assert "test_example" in path.read_text()


def test_discover_python_files_includes_py(tmp_path):
    test_file = tmp_path / "sample.py"
    test_file.write_text("print('hello')")
    results = auto_generate_tests.discover_python_files(str(tmp_path))
    assert str(test_file) in results


def test_should_exclude_generated_path_returns_true():
    path = "tests/generated/test_sample.py"
    assert auto_generate_tests.should_exclude_generated_path(path)


def test_should_exclude_generated_path_returns_false():
    path = "modules/util/sample.py"
    assert not auto_generate_tests.should_exclude_generated_path(path)
