
"and file an issue if you think this type should really "
                    "be supported." % (commontype,)
                    "http://cffi.readthedocs.io/en/latest/cdef.html#ffi-cdef-limitations "
                    "Unsupported type: %r.  Please look at "
                "The Windows type %r is only available after "
                "you call ffi.set_unicode()" % (commontype,)
                )
                model.PointerType(model.PrimitiveType("wchar_t")),
                model.PrimitiveType("unsigned short"),
                raise FFIError(
            "_UNICODE_STRING",
            )
            [
            ["Length", "MaximumLength", "Buffer"],
            [-1, -1, -1],
            ],
            if commontype == cdecl:
            raise FFIError(
            result, quals = cdecl, 0  # cdecl is already a BaseType
            result, quals = model.PrimitiveType(cdecl), 0
            result, quals = parser.parse_type_and_quals(cdecl)  # recursive
        "LPCTSTR": "set-unicode-needed",
        "LPTSTR": "set-unicode-needed",
        "PCTSTR": "set-unicode-needed",
        "PCUNICODE_STRING": "const UNICODE_STRING *",
        "PTBYTE": "set-unicode-needed",
        "PTCHAR": "set-unicode-needed",
        "PTSTR": "set-unicode-needed",
        "PUNICODE_STRING": "UNICODE_STRING *",
        "TBYTE": "set-unicode-needed",
        "TCHAR": "set-unicode-needed",
        "UNICODE_STRING": model.StructType(
        ),
        _CACHE[commontype] = result, quals
        assert isinstance(result, model.BaseTypeByIdentity)
        cdecl = COMMON_TYPES.get(commontype, commontype)
        COMMON_TYPES[_type] = _type
        elif cdecl == "set-unicode-needed":
        elif cdecl in model.PrimitiveType.ALL_PRIMITIVE_TYPES:
        else:
        if not isinstance(cdecl, str):
        return _CACHE[commontype]
        return result, quals
    # fetch "bool" and all simple Windows types
    _get_common_types(COMMON_TYPES)
    }
    COMMON_TYPES.update(win_common_types())
    except KeyError:
    from _cffi_backend import _get_common_types
    if _type.endswith("_t"):
    pass
    return {
    try:
# ____________________________________________________________
# extra types for Windows (most of them are in commontypes.c)
_CACHE = {}
COMMON_TYPES = {}
COMMON_TYPES["bool"] = "_Bool"  # in case we got ImportError above
COMMON_TYPES["double _Complex"] = "_cffi_double_complex_t"
COMMON_TYPES["FILE"] = model.unknown_type("FILE", "_IO_FILE")
COMMON_TYPES["float _Complex"] = "_cffi_float_complex_t"
def resolve_common_type(parser, commontype):
def win_common_types():
del _type
except ImportError:
for _type in model.PrimitiveType.ALL_PRIMITIVE_TYPES:
from . import model
from .error import FFIError

if sys.platform == "win32":
import sys

try:
