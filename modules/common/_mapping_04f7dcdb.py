import os
import csv
from typing import Dict, Optional

__all__ = ["load_mapping_from_csv"]


def load_mapping_from_csv(
    csv_path: str, key_column: str = "old_path", value_column: str = "new_path"
) -> Optional[Dict[str, str]]:
    """
    Load a mapping dictionary from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.
        key_column (str): Name of the column to use as dictionary keys.
        value_column (str): Name of the column to use as dictionary values.

    Returns:
        dict: A dictionary mapping keys to values from the CSV file.
    """
    if not os.path.exists(csv_path):
        print(f"⚠️ File not found: {csv_path}")
        return None

    mapping = {}
    try:
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            if (
                key_column not in reader.fieldnames
                or value_column not in reader.fieldnames
            ):
                raise ValueError(
                    f"⚠️ Missing required columns: {key_column}, {value_column}"
                )
            for row in reader:
                key = row.get(key_column, "").strip()
                value = row.get(value_column, "").strip()
                if key:
                    mapping[key] = value
        print(f"✅ Mapping loaded from {csv_path} (Total: {len(mapping)} entries)")
        return mapping
    except Exception as e:
        print(f"⚠️ Error reading mapping CSV: {e}")
        return None


if __name__ == "__main__":
    test_path = "tests/sample_map.csv"
    result = load_mapping_from_csv(test_path)
    print(result)
