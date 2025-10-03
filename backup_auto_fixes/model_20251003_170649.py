# 📄 경로: modules/common/model.py

class DummyModel:
    def __init__(self, name: str, fields: list[str]):
        self.name = name
        self.fields = fields

    def to_dict(self) -> dict:
        return {"name": self.name, "fields": self.fields}

    def __repr__(self) -> str:
        return f"<DummyModel name={self.name}, fields={self.fields}>"


# ✅ 오류 수정: 테스트에서 요구하는 속성 추가
unknown_type = "UnknownModel"
