class DummyModel:
    def __init__(self, name: str, fields: list[str]):
        self.name = name
        self.fields = fields

    def to_dict(self) -> dict:
        return {"name": self.name, "fields": self.fields}

    def __repr__(self) -> str:
        return f"<DummyModel name={self.name}, fields={self.fields}>"


# ✅ unknown_type: 함수로 정의
def unknown_type(name: str, value: str):
    """
    commontypes_1.py 에서 호출되는 더미 타입 생성 함수
    """
    return {"name": name, "value": value}


# ✅ StructType: commontypes_1.py에서 필요로 하는 구조체 타입 정의
class StructType:
    """
    Placeholder for C-style struct representation.
    """
    def __init__(self, name: str, fields: list[str] | None = None):
        self.name = name
        self.fields = fields or []

    def to_dict(self):
        return {"name": self.name, "fields": self.fields}

    def __repr__(self):
        return f"<StructType name={self.name}, fields={self.fields}>"


# ✅ PrimitiveType: 기본 타입 집합 포함
class PrimitiveType:
    ALL_PRIMITIVE_TYPES = {"bool", "int", "float", "char", "wchar_t", "void", "double"}

    def __init__(self, name: str):
        if name not in self.ALL_PRIMITIVE_TYPES:
            raise ValueError(f"Unsupported primitive type: {name}")
        self.name = name

    def __repr__(self):
        return f"<PrimitiveType name={self.name}>"


# ✅ BaseTypeByIdentity: 더미 매핑 클래스
class BaseTypeByIdentity:
    def __init__(self, identity: str, base_type: str):
        self.identity = identity
        self.base_type = base_type

    def __repr__(self):
        return f"<BaseTypeByIdentity identity={self.identity}, base_type={self.base_type}>"
