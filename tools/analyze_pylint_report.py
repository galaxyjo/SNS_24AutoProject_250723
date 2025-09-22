import json
from collections import Counter
from pathlib import Path

log_file = Path("logs/pylint_report_0804.json")
output_file = Path("logs/pylint_critical_errors_0804.txt")

with log_file.open(encoding="utf-8") as f:
    data = json.load(f)

errors = []
counter = Counter()

for item in data:
    msg_id = item.get("message-id", "")
    path = item.get("path", "")
    line = item.get("line", "")
    msg = item.get("message", "")
    symbol = item.get("symbol", "")

    # 치명적 오류만 추출
    if msg_id.startswith(("E", "F")):
        errors.append(f"[{msg_id}] {path}:{line} → {msg} ({symbol})")
        counter[msg_id] += 1

# 결과 저장
with output_file.open("w", encoding="utf-8") as f:
    f.write("🔴 Pylint 치명 오류 목록 (E/F 계열)\n\n")
    for err in errors:
        f.write(err + "\n")

    f.write("\n📊 오류 코드 요약:\n")
    for code, count in counter.most_common():
        f.write(f"{code}: {count}\n")

print(f"✅ 분석 완료 → {output_file}")
