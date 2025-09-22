# modules/common/shell_util.py

import subprocess
from typing import Optional


def run_shell_command(command: str) -> Optional[str]:
    """Runs a shell command and returns the output as string."""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def run_command_get_code(command: str) -> int:
    """Runs a shell command and returns the exit code."""
    try:
        result = subprocess.run(command, shell=True)
        return result.returncode
    except Exception:
        return -1
