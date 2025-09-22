# modules/dm/action_result.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class ActionResult:
    success: bool
    reason: Optional[str] = None
    detail: Optional[dict] = None

    def is_successful(self) -> bool:
        return self.success

    def describe(self) -> str:
        if self.success:
            return "Action succeeded"
        return f"Action failed: {self.reason or 'Unknown reason'}"
