# modules/common/browser_core.py
from __future__ import annotations
from typing import List


class Browser:
    def __init__(self, name: str = "DefaultBrowser"):
        self.name = name

    def get_info(self) -> str:
        return f"Browser: {self.name}"

    def is_secure(self) -> bool:
        return True


class BrowsingContext:
    def __init__(self, context_id: str | None = None, parent_id: str | None = None):
        self.context_id = context_id
        self.parent_id = parent_id
        self.children: List[BrowsingContext] = []

    def add_child(self, child_context: "BrowsingContext") -> None:
        if isinstance(child_context, BrowsingContext):
            self.children.append(child_context)

    def get_children(self) -> List["BrowsingContext"]:
        return self.children

    def __repr__(self) -> str:
        return (
            f"BrowsingContext(context_id={self.context_id}, "
            f"parent_id={self.parent_id}, "
            f"children={len(self.children)})"
        )


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

    def add_window(self, user_context_id: str, data: dict) -> None:
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

    def remove_user_context(self, user_context_id: str) -> None:
        if user_context_id == "default":
            raise Exception("Cannot remove the default user context")

        self.user_contexts.pop(user_context_id, None)


def main():
    browser = Browser("CoreBrowser")
    print(browser.get_info())
    print("✅ 성공" if browser.is_secure() else "⚠️ 실패")


if __name__ == "__main__":
    main()
