import sys
from . import model
from .custom_error_types import FFIError

# ____________________________________________________________
# extra types for Windows (most of them are in commontypes.c)

_CACHE = {}
COMMON_TYPES = {}

COMMON_TYPES["bool"] = "_Bool"  # in case we got ImportError above
COMMON_TYPES["double _Complex"] = "_cffi_double_complex_t"
COMMON_TYPES["float _Complex"] = "_cffi_float_complex_t"
COMMON_TYPES["FILE"] = model.unknown_type("FILE", "_IO_FILE")


def win_common_types():
    return {
        "LPCTSTR": "set-unicode-needed",
        "LPTSTR": "set-unicode-needed",
        "PTSTR": "set-unicode-needed",
        "PCTSTR": "set-unicode-needed",
        "PTCHAR": "set-unicode-needed",
        "TCHAR": "set-unicode-needed",
        "TBYTE": "set-unicode-needed",
        "PCUNICODE_STRING": "const UNICODE_STRING *",
        "PUNICODE_STRING": "UNICODE_STRING *",
        "UNICODE_STRING": model.StructType(
            "_UNICODE_STRING",
            [
                ["Length", "MaximumLength", "Buffer"],
                [-1, -1, -1],
            ],
        ),
    }


if sys.platform == "win32":
    COMMON_TYPES.update(win_common_types())


def resolve_common_type(parser, commontype):
    if commontype in _CACHE:
        return _CACHE[commontype]

    if not isinstance(commontype, str):
        raise FFIError("Unsupported type: %r. Please use a string." % (commontype,))

    cdecl = COMMON_TYPES.get(commontype, commontype)

    if cdecl == "set-unicode-needed":
        raise FFIError(
            "The Windows type %r is only available after you call ffi.set_unicode()"
            % (commontype,)
        )

    if isinstance(cdecl, model.BaseTypeByIdentity):
        result = cdecl
        quals = 0
    elif cdecl in model.PrimitiveType.ALL_PRIMITIVE_TYPES:
        result = model.PrimitiveType(cdecl)
        quals = 0
    else:
        result, quals = parser.parse_type_and_quals(cdecl)

    assert isinstance(result, model.BaseTypeByIdentity)
    _CACHE[commontype] = result, quals
    return result, quals


def _get_common_types(COMMON_TYPES):
    try:
        from _cffi_backend import _get_common_types as backend_get
        return backend_get(COMMON_TYPES)
    except ImportError:
        for _type in model.PrimitiveType.ALL_PRIMITIVE_TYPES:
            COMMON_TYPES[_type] = _type
