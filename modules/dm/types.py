# path: modules/dm/types.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Literal, Optional

EventType = Literal["comment", "mention"]


@dataclass(slots=True)
class InboundEvent:
    id: str
    user_id: str
    text: str
    ts: float
    type: EventType
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ActionResult:
    ok: bool
    action: str
    data: Dict[str, Any] = field(default_factory=dict)
    reason: Optional[str] = None
