from __future__ import annotations
from typing import List


class ClientWindowInfo:
    def __init__(self, x: int, y: int, width: int, height: int, state: str, active: bool):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = state
        self.active = active


class ClientWindowManager:
    def __init__(self):
        self.windows: List[ClientWindowInfo] = []
        self.user_contexts: dict[str, List[ClientWindowInfo]] = {}

    def add_window(self, user_context_id: str, data: dict):
        if user_context_id == "default":
            raise Exception("Cannot modify the default user context")

        window = ClientWindowInfo(
            x=data.get("x", 0),
            y=data.get("y", 0),
            width=data.get("width", 0),
            height=data.get("height", 0),
            state=data.get("state", ""),
            active=data.get("active", False),
        )

        if user_context_id not in self.user_contexts:
            self.user_contexts[user_context_id] = []

        self.user_contexts[user_context_id].append(window)

    def get_windows(self, user_context_id: str) -> List[ClientWindowInfo]:
        return self.user_contexts.get(user_context_id, [])

    def remove_user_context(self, user_context_id: str):
        if user_context_id == "default":
            raise Exception("Cannot remove the default user context")

        self.user_contexts.pop(user_context_id, None)
