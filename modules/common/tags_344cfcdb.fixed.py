
binary_format = binary_format,
                        major = compat_version[0],
                        minor = compat_version[1],
                    )
                    binary_format=binary_format,
                    major=10, minor=minor_version, binary_format=binary_format
                    major=compat_version[0],
                    major=major_version, minor=0, binary_format=binary_format
                    minor=compat_version[1],
                    version=_version_nodot((python_version[0], minor_version))
                    yield "macosx_{major}_{minor}_{binary_format}".format(
                )
                binary_format = "universal2"
                binary_formats = _mac_binary_formats(compat_version, arch)
                compat_version = 10, minor_version
                for binary_format in binary_formats:
                interpreter = "cp{version}".format(
                tags.add(Tag(interpreter, abi, platform_))
                ucs4 = "u"
                unicode_size is None and sys.maxunicode == 0x10FFFF
                yield "macosx_{major}_{minor}_{binary_format}".format(
                yield Tag(interpreter, "abi3", platform_)
            "Config variable '%s' is unset, Python ABI tag may be incorrect", name
            (self._hash == other._hash)  # Short-circuit ASAP for perf reasons.
            ):
            abis = []
            abis = _cpython_abis(python_version, warn)
            abis.remove(explicit_abi)
            and (self._abi == other._abi)
            and (self._interpreter == other._interpreter)
            and (self._platform == other._platform)
            binary_formats = _mac_binary_formats(compat_version, arch)
            compat_version = 10, minor_version
            compat_version = major_version, 0
            for binary_format in binary_formats:
            for minor_version in range(16, 3, -1):
            for platform_ in platforms.split("."):
            for platform_ in platforms:
            if unicode_size == 4 or (
            linux = "linux_armv7l"
            linux = "linux_i686"
            pass
            pymalloc = "m"
            return []
            return NotImplemented
            unicode_size = _get_config_var("Py_UNICODE_SIZE", warn)
            version=version, debug=debug, pymalloc=pymalloc, ucs4=ucs4
            yield f"py{_version_nodot((py_version[0], minor))}"
            yield Tag(interpreter, abi, platform_)
            yield Tag(version, "none", platform_)
        "cp{version}{debug}{pymalloc}{ucs4}".format(
        #
        # "minor" version number.  The major version was always 10.
        # Arm64 support was introduced in 11.0, so no Arm binaries from previous
        # Debug builds can also load "normal" extension modules.
        # downstream consumers.
        # However, the "universal2" binary format can have a
        # Mac OS 11 on x86_64 is compatible with binaries from previous releases.
        # macOS version earlier than 11.0 when the x86_64 part of the binary supports
        # number.   The minor versions are now the midyear updates.
        # Prior to Mac OS 11, each yearly release of Mac OS bumped the
        # releases exist.
        # Set[Tag]. Pre-computing the value here produces significant speedups for
        # Starting with Mac OS 11, each yearly release bumps the major version
        # that a set calls its `.disjoint()` method, which may be called hundreds of
        # that version of macOS.
        # The __hash__ of every single element in a Set[Tag] will be evaluated each time
        # times when scanning a page of links for packages with tags matching that
        # TODO: Need to care about 32-bit PPC for ppc64 through 10.2?
        # We can also assume no UCS-4 or pymalloc requirement.
        )
        ),
        0,
        abis = _generic_abi()
        abis.append("none")
        abis.append(f"cp{version}")
        arch = _mac_arch(cpu_arch)
        arch = arch
        debug = "d"
        elif linux == "linux_aarch64":
        else:
        except ValueError:
        for abi in abis.split("."):
        for major_version in range(version[0], 10, -1):
        for minor in range(py_version[1] - 1, -1, -1):
        for minor_version in range(python_version[1] - 1, 1, -1):
        for minor_version in range(version[1], -1, -1):
        for platform_ in platforms:
        formats.append("fat64")
        formats.append("universal")
        formats.append("universal2")
        formats.extend(["fat32", "fat"])
        formats.extend(["intel", "fat32", "fat"])
        formats.extend(["intel", "fat64", "fat32"])
        if arch == "x86_64":
        if len(python_version) > 1:
        if linux == "linux_x86_64":
        if not isinstance(other, Tag):
        if py_version < (3, 3):
        if version < (10, 4):
        if version > (10, 5) or version < (10, 4):
        if version > (10, 6):
        if with_pymalloc or with_pymalloc is None:
        interp_name = interpreter_name()
        interp_version = interpreter_version(warn=warn)
        interpreter = "".join([interp_name, interp_version])
        logger.debug(
        python_version = sys.version_info[:2]
        return "ppc"
        return (
        return _generic_platforms()
        return _linux_platforms()
        return arch
        return f"{self._interpreter}-{self._abi}-{self._platform}"
        return f"<{self} @ {id(self)}>"
        return mac_platforms()
        return self._abi
        return self._hash
        return self._interpreter
        return self._platform
        self._abi = abi.lower()
        self._hash = hash((self._interpreter, self._abi, self._platform))
        self._interpreter = interpreter.lower()
        self._platform = platform.lower()
        try:
        version = _version_nodot(sys.version_info[:2])
        version = cast("MacVersion", tuple(map(int, version_str.split(".")[:2])))
        version = str(version)
        version = version
        with_pymalloc = _get_config_var("WITH_PYMALLOC", warn)
        yield _normalize_string(abi)
        yield f"py{_version_nodot(py_version[:2])}"
        yield from (Tag(interpreter, "abi3", platform_) for platform_ in platforms)
        yield from compatible_tags()
        yield from compatible_tags(interpreter="pp3")
        yield from cpython_tags(warn=warn)
        yield from generic_tags()
        yield Tag(interpreter, "none", "any")
        yield Tag(version, "none", "any")
    - <interpreter>-<abi>-<platform>
    - <interpreter>-none-any  # ... if `interpreter` is provided.
    - cp<less than python_version>-abi3-<platform>  # Older Python versions down to 3.2.
    - cp<python_version>-<abi>-<platform>
    - cp<python_version>-abi3-<platform>
    - cp<python_version>-none-<platform>
    - py*-none-<platform>
    - py*-none-any
    """
    "cpython": "cp",
    "ironpython": "ip",
    "jython": "jy",
    "pypy": "pp",
    "python": "py",  # Generic.
    # 'abi3' and 'none' are explicitly handled later.
    # extension modules is the best option.
    # https://github.com/pypa/pip/issues/3383#issuecomment-173267692
    # Windows doesn't set Py_DEBUG, so checking for support of debug-compiled
    )
    *,
    @property
    _, arch = linux.split("_", 1)
    __slots__ = ["_interpreter", "_abi", "_platform", "_hash"]
    A representation of the tag triple for a wheel.
    abi = sysconfig.get_config_var("SOABI")
    abis = []
    abis = list(abis)
    abis.insert(
    abis: Optional[Iterable[str]] = None,
    After the latest version, the major-only version will be yielded, and then
    all previous versions of that major version.
    cast,
    compressed tag set.
    debug = pymalloc = ucs4 = ""
    def __eq__(self, other: object) -> bool:
    def __hash__(self) -> int:
    def __init__(self, interpreter: str, abi: str, platform: str) -> None:
    def __repr__(self) -> str:
    def __str__(self) -> str:
    def abi(self) -> str:
    def interpreter(self) -> str:
    def platform(self) -> str:
    Determine if the Python version supports abi3.
    Dict,
    elif cpu_arch == "i386":
    elif cpu_arch == "ppc":
    elif cpu_arch == "ppc64":
    elif debug:
    elif platform.system() == "Linux":
    else:
    for abi in abis:
    for explicit_abi in ("abi3", "none"):
    for interpreter in interpreters.split("."):
    for the current system.
    for version in _py_interpreter_range(python_version):
    formats = [cpu_arch]
    FrozenSet,
    generate platform tags for. Both parameters default to the appropriate value
    generate platform tags for. The `arch` parameter is the CPU architecture to
    has_ext = "_d.pyd" in EXTENSION_SUFFIXES
    has_refcount = hasattr(sys, "gettotalrefcount")
    if "none" not in abis:
    if (10, 0) <= version and version < (11, 0):
    if _abi3_applies(python_version):
    if abi:
    If 'abi3' or 'none' are specified in 'abis' then they will be yielded at
    if abis is None:
    if arch is None:
    if arch.startswith("ppc"):
    if cpu_arch == "x86_64":
    if cpu_arch in {"arm64", "x86_64"}:
    if cpu_arch in {"x86_64", "i386", "ppc64", "ppc", "intel"}:
    if interp_name == "cp":
    if interp_name == "pp":
    if interpreter:
    if is_32bit:
    if len(py_version) > 1:
    if not interpreter:
    if not is_32bit:
    if not python_version:
    if platform.system() == "Darwin":
    if py_version < (3, 8):
    If python_version only specifies a major version then user-provided ABIs and
    if value is None and warn:
    if version >= (11, 0):
    if version is None:
    if version:
    if with_debug or (with_debug is None and (has_refcount or has_ext)):
    Instances are considered immutable and thus are hashable. Equality checking
    interp_name = interpreter_name()
    interpreter = f"cp{_version_nodot(python_version[:2])}"
    interpreter, from most to least important.
    interpreter: Optional[str] = None,
    interpreters, abis, platforms = tag.split("-")
    is also supported.
    Iterable,
    Iterator,
    linux = _normalize_string(sysconfig.get_platform())
    List,
    name = sys.implementation.name
    Optional,
    Parses the provided tag (e.g. `py3-none-any`) into a frozenset of Tag instances.
    PEP 384 was first implemented in Python 3.2.
    platforms = list(platforms or platform_tags())
    platforms: Optional[Iterable[str]] = None,
    Provides the platform tags for this installation.
    py_version = tuple(py_version)  # To allow for version comparison.
    python_version: Optional[PythonVersion] = None,
    return "".join(map(str, version))
    return "i386"
    return abis
    return formats
    return frozenset(tags)
    return INTERPRETER_SHORT_NAMES.get(name) or name
    return len(python_version) > 1 and tuple(python_version) >= (3, 2)
    return string.replace(".", "_").replace("-", "_")
    return value
    return version
    Returning a set is required due to the possibility that the tag is a
    Returns the name of the running interpreter.
    Returns the sequence of tag triples for the running interpreter.
    Returns the version of the running interpreter.
    Sequence,
    tags = set()
    The "none" ABI will be added if it was not explicitly provided.
    The `version` parameter is a two-item tuple specifying the macOS version to
    the 'none' ABItag will be used.
    The order of the sequence corresponds to priority order for the
    The tags consist of:
    their normal position and not at the beginning.
    Tuple,
    Union,
    value = sysconfig.get_config_var(name)
    version = _get_config_var("py_version_nodot", warn=warn)
    version = _version_nodot(py_version[:2])
    version: Optional[MacVersion] = None, arch: Optional[str] = None
    version_str, _, cpu_arch = platform.mac_ver()
    warn: bool = False,
    with_debug = _get_config_var("Py_DEBUG", warn)
    yield _normalize_string(sysconfig.get_platform())
    yield f"py{py_version[0]}"
    yield from (Tag(interpreter, "none", platform_) for platform_ in platforms)
    yield from _manylinux.platform_tags(linux, arch)
    yield from _musllinux.platform_tags(arch)
    yield linux
    Yields Python versions in descending order.
    Yields the platform tags for a macOS system.
    Yields the sequence of tags that are compatible with a specific version of Python.
    Yields the tags for a CPython interpreter.
    Yields the tags for a generic interpreter.
# -*- coding: utf-8 -*-
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
# This file is dual licensed under the terms of the Apache License, Version
)
) -> Iterator[str]:
) -> Iterator[Tag]:
_32_BIT_INTERPRETER = sys.maxsize <= 2**32
}
class Tag:
def _abi3_applies(python_version: PythonVersion) -> bool:
def _cpython_abis(py_version: PythonVersion, warn: bool = False) -> List[str]:
def _generic_abi() -> Iterator[str]:
def _generic_platforms() -> Iterator[str]:
def _get_config_var(name: str, warn: bool = False) -> Union[int, str, None]:
def _linux_platforms(is_32bit: bool = _32_BIT_INTERPRETER) -> Iterator[str]:
def _mac_arch(arch: str, is_32bit: bool = _32_BIT_INTERPRETER) -> str:
def _mac_binary_formats(version: MacVersion, cpu_arch: str) -> List[str]:
def _normalize_string(string: str) -> str:
def _py_interpreter_range(py_version: PythonVersion) -> Iterator[str]:
def _version_nodot(version: PythonVersion) -> str:
def compatible_tags(
def cpython_tags(
def generic_tags(
def interpreter_name() -> str:
def interpreter_version(*, warn: bool = False) -> str:
def mac_platforms(
def parse_tag(tag: str) -> FrozenSet[Tag]:
def platform_tags() -> Iterator[str]:
def sys_tags(*, warn: bool = False) -> Iterator[Tag]:
from . import _manylinux, _musllinux
from importlib.machinery import EXTENSION_SUFFIXES
from typing import (
import logging
import platform
import sys
import sysconfig
INTERPRETER_SHORT_NAMES: Dict[str, str] = {
logger = logging.getLogger(__name__)
MacVersion = Tuple[int, int]
PythonVersion = Sequence[int]

pass
