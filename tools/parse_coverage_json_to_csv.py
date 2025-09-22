import sys
import json
import csv
from pathlib import Path


def parse_coverage_json(json_path, output_csv):
    json_path = Path(json_path)
    output_csv = Path(output_csv)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    coverage_data = data.get("files", {})
    rows = []

    for filepath, metrics in coverage_data.items():
        summary = metrics.get("summary", {})
        rows.append(
            {
                "filename": filepath,
                "statements": summary.get("num_statements", 0),
                "missing": summary.get("missing_lines", 0),
                "excluded": summary.get("excluded_lines", 0),
                "percent_covered": round(summary.get("percent_covered", 0.0), 2),
            }
        )

    rows.sort(key=lambda r: r["percent_covered"])  # 낮은 커버리지부터 정렬

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"[✅ 완료] CSV 저장: {output_csv.resolve()}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "사용법: python parse_coverage_json_to_csv.py <coverage.json 경로> <출력 CSV 경로>"
        )
        sys.exit(1)

    parse_coverage_json(sys.argv[1], sys.argv[2])
