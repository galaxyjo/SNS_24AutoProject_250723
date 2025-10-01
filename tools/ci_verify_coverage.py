"""Coverage CSV Checker for CI."""

import csv
import sys
import os

COVERAGE_FILE = "coverage/coverage_summary.csv"
MIN_COVERAGE = 80.0  # 기준 퍼센트

if not os.path.exists(COVERAGE_FILE):
    print(f"❌ {COVERAGE_FILE} not found.")
    sys.exit(1)

with open(COVERAGE_FILE, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        coverage = float(row.get("Coverage", 0))
        module = row.get("Module", "Unknown")
        if coverage < MIN_COVERAGE:
            print(
                f"❌ FAIL: {module} coverage {coverage:.2f}% < {MIN_COVERAGE}%"
            )  # ✅ 이 줄이 79자 이하로 줄였음
            sys.exit(1)

print("✅ All modules meet coverage threshold.")
