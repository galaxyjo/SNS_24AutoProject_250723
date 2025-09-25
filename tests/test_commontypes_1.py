import sys
import pytest
from modules.common import commontypes_1
from modules.common.model import StructType, PrimitiveType, BaseTypeByIdentity


class DummyParser:
    def parse_type_and_quals(self, cdecl):
        return PrimitiveType(cdecl), 0


def test_resolve_known_primitive_type():
    parser = DummyParser()
    result, quals = commontypes_1.resolve_common_type(parser, "bool")
    assert isinstance(result, BaseTypeByIdentity)
    assert quals == 0


def test_resolve_unknown_type_should_fail():
    parser = DummyParser()
    with pytest.raises(commontypes_1.FFIError):
        commontypes_1.resolve_common_type(parser, 1234)


def test_resolve_win_unicode_error():
    parser = DummyParser()
    if sys.platform == "win32":
        with pytest.raises(commontypes_1.FFIError):
            commontypes_1.resolve_common_type(parser, "TCHAR")


def test_unicode_struct_type_exists():
    if sys.platform == "win32":
        result = commontypes_1.COMMON_TYPES.get("UNICODE_STRING")
        assert isinstance(result, StructType)
        assert result.fields[0] == ["Length", "MaximumLength", "Buffer"]
