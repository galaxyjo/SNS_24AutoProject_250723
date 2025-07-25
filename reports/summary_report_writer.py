
            f.write(str(line) + "\n")
        for line in data:
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, f"{prefix}_{ts}.txt")
    print(f"📄 저장됨: {path}")
    return path
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(path, "w", encoding="utf-8") as f:
# reporting/summary_report_writer.py
def save_log(data, prefix, log_dir):
from datetime import datetime
import os
