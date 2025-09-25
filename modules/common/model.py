class DummyModel:
    def __init__(self, name: str, fields: list[str]):
        self.name = name
        self.fields = fields

    def to_dict(self) -> dict:
        return {"name": self.name, "fields": self.fields}

    def __repr__(self) -> str:
        return f"<DummyModel name={self.name}, fields={self.fields}>"
