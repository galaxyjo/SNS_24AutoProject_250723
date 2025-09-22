import csv
import yaml
import sys
from typing import Dict


def load_thresholds(threshold_path: str) -> Dict[str, float]:
    with open(threshold_path, "r", encoding="utf-8") as f:
        thresholds = yaml.safe_load(f)
    return thresholds or {}


def check_coverage(summary_path: str, thresholds_path: str) -> bool:
    thresholds = load_thresholds(thresholds_path)
    failed = False

    with open(summary_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            module = row["file"]
            try:
                coverage = float(row["summary_percent"])
            except (KeyError, ValueError):
                print(f"⚠️  잘못된 커버리지 값: {row}")
                continue

            threshold = thresholds.get(module, thresholds.get("default", 0.0))
            if coverage < threshold:
                print(f"❌ {module}: {coverage}% < 기준 {threshold}%")
                failed = True
            else:
                print(f"✅ {module}: {coverage}% ≥ 기준 {threshold}%")

    return failed


def main():
    if len(sys.argv) != 3:
        print(
            "사용법: python check_coverage_thresholds.py <coverage_summary.csv> <thresholds.yaml>"
        )
        sys.exit(1)

    summary_path = sys.argv[1]
    thresholds_path = sys.argv[2]

    failed = check_coverage(summary_path, thresholds_path)
    if failed:
        sys.exit(1)
    else:
        print("🎉 모든 모듈 커버리지 기준 통과!")


if __name__ == "__main__":
    main()
