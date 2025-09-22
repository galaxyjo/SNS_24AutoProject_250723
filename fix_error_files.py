# fix_error_files.py
# -*- coding: utf-8 -*-
"""
pytest 마지막 실행 에러 로그에서
에러 발생한 .py 파일만 찾아서 자동 교정 + IndentationError 보정
"""
import io
import os
import re
import subprocess

BASE = os.path.abspath(os.getcwd())
LOG_FILE = os.path.join(BASE, "last_pytest.log")


def run_pytest():
    """pytest 실행 후 로그 저장"""
    cmd = ["pytest", "-v", "-k", "not ssl_handler", "--maxfail=1"]
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )
        for line in proc.stdout:
            print(line, end="")  # 화면 출력
            f.write(line)
    proc.wait()


def parse_error_files():
    """pytest 로그에서 에러난 파일 경로 추출 + IndentationError 위치"""
    error_files = set()
    indent_errors = []  # (path, lineno)
    if not os.path.exists(LOG_FILE):
        return [], []
    with io.open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        last_path = None
        for line in f:
            m_file = re.search(r'File "(.+?\.py)", line (\d+)', line)
            if m_file:
                last_path = os.path.abspath(m_file.group(1))
                if os.path.exists(last_path):
                    error_files.add(last_path)
            m_indent = re.search(r"IndentationError: .*", line)
            if m_indent and last_path:
                lineno_match = re.search(r"line (\d+)", line)
                if lineno_match:
                    indent_errors.append((last_path, int(lineno_match.group(1))))
    return sorted(error_files), indent_errors


def read_file(path):
    with io.open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def write_file(path, text):
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def fix_indentation(path, lineno):
    """간단한 들여쓰기 보정: try/except 블록 안쪽으로 정렬"""
    lines = read_file(path).split("\n")
    idx = lineno - 1
    if 0 <= idx < len(lines):
        target_line = lines[idx]
        # 들여쓰기 레벨 계산
        prev_indent = ""
        # 위쪽에서 가까운 try:/except 찾기
        for up in range(idx - 1, -1, -1):
            if re.match(r"^\s*(try:|except\b|else:|finally:)", lines[up]):
                prev_indent = re.match(r"^\s*", lines[up]).group(0) + "    "
                break
        # 기본 4칸 들여쓰기
        if not prev_indent:
            prev_indent = "    "
        fixed_line = prev_indent + target_line.lstrip()
        lines[idx] = fixed_line
        write_file(path, "\n".join(lines))
        print(f"🔧 들여쓰기 수정 → {path}:{lineno}")


def fix_file(path):
    txt = read_file(path)
    orig = txt

    # 줄끝 백틱 제거
    txt = re.sub(r"`\s*$", "", txt, flags=re.M)

    # 키워드 오타
    txt = re.sub(r"(?m)^\s*mport\b", "import", txt)
    txt = re.sub(r"(?m)^\s*imprt\b", "import", txt)
    txt = re.sub(r"(?m)^\s*fom\b", "from", txt)
    txt = re.sub(r"(?m)^\s*frm\b", "from", txt)
    txt = re.sub(r"(?m)^\s*ry:\b", "try:", txt)
    txt = re.sub(
        r"(?mi)^\s*rom\s+__future__\s+import\s+absolute_import\s*$",
        "from __future__ import absolute_import",
        txt,
    )

    # import 경로 표준화
    txt = re.sub(
        r"(^|\n)\s*import\s+time_helper\s*(?=\n|$)",
        r"\1from modules.common import time_helper",
        txt,
    )
    txt = re.sub(
        r"(^|\n)\s*from\s+time_helper\s+import\s+([^\n]+)",
        r"\1from modules.common.time_helper import \2",
        txt,
    )

    # try: pass 한줄 → 멀티라인 + except
    txt = re.sub(
        r"(?m)^(?P<ind>[ \t]*)try:\s+pass\s*$",
        lambda m: f"{m.group('ind')}try:\n{m.group('ind')}    pass\n{m.group('ind')}except Exception:\n{m.group('ind')}    pass",
        txt,
    )

    if txt != orig:
        write_file(path, txt)
        print(f"✏ 수정 완료 → {path}")
    else:
        print(f"ℹ 변경 없음 → {path}")


def main():
    run_pytest()
    files, indent_errors = parse_error_files()
    if not files:
        print("✅ 에러 파일 없음 - 교정할 대상이 없습니다.")
        return

    print("🔍 교정 대상:")
    for f in files:
        print(" -", f)
        fix_file(f)

    # 들여쓰기 에러 보정
    for path, lineno in indent_errors:
        fix_indentation(path, lineno)

    print("✅ 부분 교정 + 들여쓰기 보정 완료")


if __name__ == "__main__":
    main()
