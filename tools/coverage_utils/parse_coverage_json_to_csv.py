# 파일명: tools/coverage_utils/parse_coverage_json_to_csv.py
import json
import csv
import sys


def parse_coverage_json_to_csv(input_json, output_csv):
    with open(input_json, "r") as f:
        data = json.load(f)

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "statements", "missed", "coverage"])

        files = data.get("files", {})
        for path, file_data in files.items():
            summary = file_data.get("summary", {})
            statements = summary.get("num_statements", 0)
            missed = summary.get("missing_lines", 0)
            covered = 100 - (missed / statements * 100) if statements else 0
            writer.writerow([path, statements, missed, f"{covered:.2f}%"])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: parse_coverage_json_to_csv.py <input.json> <output.csv>")
        sys.exit(1)
    parse_coverage_json_to_csv(sys.argv[1], sys.argv[2])
