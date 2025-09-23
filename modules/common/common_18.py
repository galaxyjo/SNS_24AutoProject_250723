from typing import Any

class Common18:
    def __init__(self):
        self.data = {}

    def add_entry(self, key: str, value: Any) -> None:
        self.data[key] = value

    def get_entry(self, key: str) -> Any:
        return self.data.get(key)

    def remove_entry(self, key: str) -> None:
        if key in self.data:
            del self.data[key]

    def clear_entries(self) -> None:
        self.data.clear()

    def get_all_entries(self) -> dict:
        return self.data
