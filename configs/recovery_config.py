
# config/recovery_config.py
import os
BASE_DIR = r"C:\clean_rebuild"
EXCLUDE_DIRS = ["__pycache__", "site-packages", "venv"]
FUNCTIONS_TO_TRACE = ["connect_to_server", "send_data", "receive_data"]
LOG_DIR = os.path.join(BASE_DIR, "logs", "trace")
MAIN_PY = os.path.join(BASE_DIR, "launcher", "main.py")
SNAPSHOT_CSV = os.path.join(BASE_DIR, "snapshots", "master_hash.csv")
