import os
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
GENERATED_DIR = ROOT_DIR / "tests" / "generated"
PYTEST_INI = ROOT_DIR / "pytest.ini"


def find_generated_test_files():
    failures = []
    for root, _, files in os.walk(ROOT_DIR / "tests"):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                file_path = Path(root) / file
                rel_path = file_path.relative_to(ROOT_DIR)
                if "generated" not in rel_path.parts:
                    with open(file_path, encoding="utf-8") as f:
                        content = f.read()
                        if "# AUTO-GENERATED" in content:
                            failures.append(str(rel_path))
    return failures


def find_headers_in_generated_tests():
    missing_header = []
    missing_pragma = []

    for root, _, files in os.walk(GENERATED_DIR):
        for file in files:
            if file.endswith(".py"):
                file_path = Path(root) / file
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()
                    if "# AUTO-GENERATED" not in content:
                        missing_header.append(str(file_path))
                    if "# pragma: no cover" not in content:
                        missing_pragma.append(str(file_path))
    return missing_header, missing_pragma


def pytest_ini_configured():
    if not PYTEST_INI.exists():
        return False
    with open(PYTEST_INI, encoding="utf-8") as f:
        content = f.read()
        return "norecursedirs" in content and "tests/generated" in content


class TestSafetyChecker(unittest.TestCase):
    def test_generated_test_files(self):
        failures = find_generated_test_files()
        self.assertEqual(
            failures, [], f"잘못된 위치의 자동 생성 테스트 발견: {failures}"
        )

    def test_headers_in_generated_tests(self):
        missing_header, missing_pragma = find_headers_in_generated_tests()
        self.assertEqual(missing_header, [], f"헤더 누락 파일 발견: {missing_header}")
        self.assertEqual(missing_pragma, [], f"pragma 누락 파일 발견: {missing_pragma}")

    def test_pytest_ini(self):
        self.assertTrue(pytest_ini_configured(), "pytest.ini 설정이 올바르지 않음")


if __name__ == "__main__":
    unittest.main()
