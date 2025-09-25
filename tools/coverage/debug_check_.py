import csv
import sys
import yaml

def check_coverage(summary_path, thresholds_path):
    with open(thresholds_path, "r") as f:
        thresholds = yaml.safe_load(f)

    failed = []
    with open(summary_path, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            path = row["filename"]  # ✅ 기존 'file' → 'filename'
            covered = float(row["percent_covered"])
            threshold = thresholds.get(path, thresholds.get("default", 0.0))
            if covered < threshold:
                failed.append((path, covered, threshold))

    return failed

def main():
    if len(sys.argv) != 3:
        print("Usage: python debug_check.py <coverage_summary.csv> <thresholds.yaml>")
        sys.exit(1)

    summary_path = sys.argv[1]
    thresholds_path = sys.argv[2]

    failed = check_coverage(summary_path, thresholds_path)

    if failed:
        print("\n❌ Threshold FAIL (coverage below threshold):")
        for path, covered, threshold in failed:
            print(f"  - {path}: {covered:.1f}% < {threshold:.1f}%")
        sys.exit(1)
    else:
        print("✅ Threshold PASS")

if __name__ == "__main__":
    main()
