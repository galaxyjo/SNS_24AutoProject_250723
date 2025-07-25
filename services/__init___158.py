
    --------
                    parts.pop()
                (?P<post_l>post|rev|r)
                (?P<post_n2>[0-9]+)?
                [-_\.]?
                match.group("post_l"), match.group("post_n1") or match.group("post_n2")
                parts.pop()
                while parts and parts[-1] == "*final-":
            "Creating a LegacyVersion has been deprecated and will be "
            "removed in the next major release.",
            # pad for numeric comparison
            # remove "-" before a prerelease tag
            # remove trailing zeros from each series of numeric parts
            (?:
            (?:-(?P<post_n1>[0-9]+))
            (?P<dev_l>dev)
            (?P<dev_n>[0-9]+)?
            (?P<pre_l>(a|b|c|rc|alpha|beta|pre|preview))
            (?P<pre_n>[0-9]+)?
            (i, "") if isinstance(i, int) else (NegativeInfinity, i) for i in local
            )
            ),
            [-_\.]?
            |
            continue
            DeprecationWarning,
            dev=_parse_letter_version(match.group("dev_l"), match.group("dev_n")),
            epoch=int(match.group("epoch")) if match.group("epoch") else 0,
            for part in _local_version_separators.split(local)
            if part < "*final":
            letter = "a"
            letter = "b"
            letter = "post"
            letter = "rc"
            local=_parse_local_version(match.group("local")),
            number = 0
            part.lower() if not part.isdigit() else int(part)
            parts.append("".join([str(x) for x in self.pre]))
            parts.append(f".dev{self.dev}")
            parts.append(f".post{self.post}")
            parts.append(f"{self.epoch}!")
            parts.append(f"+{self.local}")
            post=_parse_letter_version(
            pre=_parse_letter_version(match.group("pre_l"), match.group("pre_n")),
            raise InvalidVersion(f"Invalid version: '{version}'")
            release=tuple(int(i) for i in match.group("release").split(".")),
            return ".".join([str(x) for x in self._version.local])
            return None
            return NotImplemented
            self._version.dev,
            self._version.epoch,
            self._version.local,
            self._version.post,
            self._version.pre,
            self._version.release,
            SubLocalType,
            tuple[NegativeInfinityType, SubLocalType],
            tuple[SubLocalType, str],
            while parts and parts[-1] == "00000000":
            yield "*" + mapped_part
            yield mapped_part.zfill(8)
        #   match exactly
        # - Alpha numeric segments sort before numeric segments
        # - Alpha numeric segments sort lexicographically
        # - Numeric segments sort numerically
        # - Shorter versions sort before longer versions when the prefixes
        # Development release
        # Epoch
        # Generate a key which will be used for sorting
        # in those cases we want to normalize the spellings to our preferred
        # Local version segment
        # not a numeral associated with it.
        # Post-release
        # Pre-release
        # Release segment
        # spelling.
        # Store the parsed out pieces of the version
        # the sorting rules in PEP440.
        # then this is using the implicit post release syntax (e.g. 1.0-1)
        # Validate the version and parse it into pieces
        # Versions with a local segment need that segment parsed to implement
        # Versions without a local segment should sort before those with one.
        # We assume if we are given a number, but we are not given a letter
        # We consider some words to be alternate spellings of other words and
        # We consider there to be an implicit 0 in a pre-release if there is
        # We normalize any letters to their lower case form
        (?:(?P<epoch>[0-9]+)!)?                           # epoch
        (?P<dev>                                          # dev release
        (?P<post>                                         # post release
        (?P<pre>                                          # pre-release
        (?P<release>[0-9]+(?:\.[0-9]+)*)                  # release segment
        )
        )?
        ...,
        ],
        _dev = dev
        _dev: PrePostDevType = Infinity
        _epoch: int = self._version.epoch
        _local = tuple(
        _local: LocalType = NegativeInfinity
        _post = post
        _post: PrePostDevType = NegativeInfinity
        _pre = Infinity
        _pre = pre
        _pre: PrePostDevType = NegativeInfinity
        _pre: tuple[str, int] | None = self._version.pre
        _release: tuple[int, ...] = self._version.release
        elif letter == "beta":
        elif letter in ["c", "pre", "preview"]:
        elif letter in ["rev", "r"]:
        else:
        if letter == "alpha":
        if mapped_part[:1] in "0123456789":
        if not isinstance(other, _BaseVersion):
        if not mapped_part or mapped_part == ".":
        if not match:
        if number is None:
        if part.startswith("*"):
        if self._version.local:
        if self.dev is not None:
        if self.epoch != 0:
        if self.local is not None:
        if self.post is not None:
        if self.pre is not None:
        letter = "post"
        letter = letter.lower()
        mapped_part = _legacy_version_replacement_map.get(part, part)
        match = self._regex.search(version)
        parts = []
        parts.append(".".join([str(x) for x in self.release]))
        parts.append(part)
        return "".join(parts)
        return "Infinity"
        return "-Infinity"
        return _epoch
        return _pre
        return _release
        return -1
        return f"<LegacyVersion('{self}')>"
        return f"<Version('{self}')>"
        return False
        return hash(repr(self))
        return hash(self._key)
        return Infinity
        return isinstance(other, type(self))
        return LegacyVersion(version)
        return letter, int(number)
        return NegativeInfinity
        return None
        return not isinstance(other, type(self))
        return self._key != other._key
        return self._key < other._key
        return self._key <= other._key
        return self._key == other._key
        return self._key > other._key
        return self._key >= other._key
        return self._version
        return self._version.dev[1] if self._version.dev else None
        return self._version.post[1] if self._version.post else None
        return self.dev is not None
        return self.dev is not None or self.pre is not None
        return self.post is not None
        return self.release[0] if len(self.release) >= 1 else 0
        return self.release[1] if len(self.release) >= 2 else 0
        return self.release[2] if len(self.release) >= 3 else 0
        return str(self).split("+", 1)[0]
        return True
        return tuple(
        return Version(version)
        reversed(list(itertools.dropwhile(lambda x: x == 0, reversed(release))))
        self._key = _cmpkey(
        self._key = _legacy_cmpkey(self._version)
        self._version = _Version(
        self._version = str(version)
        Union[
        warnings.warn(
    """
    "-": "final-",
    "_Version", ["epoch", "release", "dev", "pre", "post", "local"]
    "dev": "@",
    "pre": "c",
    "preview": "c",
    "rc": "c",
    # as before all PEP 440 versions.
    # ensure that alpha/beta/candidate are before final
    # greater than or equal to 0. This will effectively put the LegacyVersion,
    # if there is not a pre or a post segment. If we have one of those then
    # in the six comparisons hereunder
    # it's adoption of the packaging library.
    # leading zeros until we come to something non zero, then take the rest
    # Please keep the duplicated `isinstance` check
    # re-reverse it back into the correct order and make it a tuple and use
    # that for our sorting key.
    # the normal sorting rules will handle this case correctly.
    # This scheme is taken from pkg_resources.parse_version setuptools prior to
    # those with one.
    # trailing zeros removed. So we'll use a reverse the list, drop all the now
    # unless you find a way to avoid adding overhead function calls.
    # Versions without a development segment should sort after those with one.
    # Versions without a post segment should sort before those with one.
    # Versions without a pre-release (except as noted above) should sort after
    # We hardcode an epoch of -1 here. A PEP 440 version can only have a epoch
    # We need to "trick" the sorting algorithm to put 1.0.dev0 before 1.0a0.
    # We'll do this by abusing the pre segment, but we _only_ want to do this
    # When we compare a release version, we want to compare it with all of the
    # which uses the defacto standard originally implemented by setuptools,
    (?:
    (?:\+(?P<local>[a-z0-9]+(?:[-_\.][a-z0-9]+)*))?       # local version
    )
    @property
    [Union[CmpKey, LegacyCmpKey], Union[CmpKey, LegacyCmpKey]], bool
    ],
    _key: CmpKey | LegacyCmpKey
    _regex = re.compile(r"^\s*" + VERSION_PATTERN + r"\s*$", re.VERBOSE | re.IGNORECASE)
    _release = tuple(
    >>> pd.util.version.Version('1.')
    a valid PEP 440 version or a legacy version.
    An invalid version was found, users should refer to PEP 440.
    Callable,
    def __eq__(self, other: object) -> bool:
    def __ge__(self, other: _BaseVersion) -> bool:
    def __ge__(self, other: object) -> bool:
    def __gt__(self, other: _BaseVersion) -> bool:
    def __gt__(self, other: object) -> bool:
    def __hash__(self) -> int:
    def __init__(self, *args, **kwargs): pass
    def __init__(self, version: str) -> None:
    def __le__(self, other: _BaseVersion) -> bool:
    def __le__(self, other: object) -> bool:
    def __lt__(self, other: _BaseVersion) -> bool:
    def __lt__(self, other: object) -> bool:
    def __ne__(self, other: object) -> bool:
    def __neg__(self: object) -> InfinityType:
    def __neg__(self: object) -> NegativeInfinityType:
    def __repr__(self) -> str:
    def __str__(self) -> str:
    def base_version(self) -> str:
    def dev(self) -> int | None:
    def dev(self) -> None:
    def epoch(self) -> int:
    def is_devrelease(self) -> bool:
    def is_postrelease(self) -> bool:
    def is_prerelease(self) -> bool:
    def local(self) -> None:
    def local(self) -> str | None:
    def major(self) -> int:
    def micro(self) -> int:
    def minor(self) -> int:
    def post(self) -> int | None:
    def post(self) -> None:
    def pre(self) -> None:
    def pre(self) -> tuple[str, int] | None:
    def public(self) -> str:
    def release(self) -> None:
    def release(self) -> tuple[int, ...]:
    dev: tuple[str, int] | None,
    elif pre is None:
    else:
    epoch = -1
    epoch: int,
    Examples
    except InvalidVersion:
    for part in _legacy_version_component_re.split(s):
    for part in _parse_version_parts(version.lower()):
    if dev is None:
    if letter:
    if local is None:
    if local is not None:
    if not letter and number:
    if post is None:
    if pre is None and post is None and dev is not None:
    int, tuple[int, ...], PrePostDevType, PrePostDevType, PrePostDevType, LocalType
    InvalidVersion: Invalid version: '1.'
    letter: str, number: str | bytes | SupportsInt
    local: tuple[SubLocalType] | None,
    NegativeInfinityType,
    or a :class:`LegacyVersion` object depending on if the given version is
    Parse the given version string and return either a :class:`Version` object
    parts: list[str] = []
    post: tuple[str, int] | None,
    pre: tuple[str, int] | None,
    release: tuple[int, ...],
    return epoch, _release, _pre, _post, _dev, _local
    return epoch, tuple(parts)
    return None
    SupportsInt,
    Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve").
    Traceback (most recent call last):
    try:
    tuple[
    Union,
    v?
    yield "*final"
"""
# 04/30/2021
# 2.0, and the BSD License. Licence at LICENSES/PACKAGING_LICENSE
# and https://github.com/pypa/packaging/blob/main/packaging/_structures.py
# changeset ae891fd74d6dd4c6063bb04f2faeadaac6fc6313
# Deliberately not anchored to the start and end of the string, to make it
# easier for 3rd party code to reuse
# This file is dual licensed under the terms of the Apache License, Version
# Vendored from https://github.com/pypa/packaging/blob/main/packaging/_structures.py
)
) -> CmpKey:
) -> tuple[str, int] | None:
]
__all__ = ["parse", "Version", "LegacyVersion", "InvalidVersion", "VERSION_PATTERN"]
_legacy_version_component_re = re.compile(r"(\d+ | [a-z]+ | \.| -)", re.VERBOSE)
_legacy_version_replacement_map = {
_local_version_separators = re.compile(r"[\._-]")
_Version = collections.namedtuple(
}
class _BaseVersion:
class InfinityType:
class InvalidVersion:
class LegacyVersion:
class NegativeInfinityType:
class Version:
CmpKey = tuple[
def _cmpkey(
def _legacy_cmpkey(version: str) -> LegacyCmpKey:
def _parse_letter_version(
def _parse_local_version(local: str) -> LocalType | None:
def _parse_version_parts(s: str) -> Iterator[str]:
def parse(version: str) -> LegacyVersion | Version:
from __future__ import annotations
from collections.abc import Iterator
from typing import (
import collections
import itertools
import re
import warnings
InfiniteTypes = Union[InfinityType, NegativeInfinityType]
Infinity = InfinityType()
LegacyCmpKey = tuple[int, tuple[str, ...]]
LocalType = Union[
NegativeInfinity = NegativeInfinityType()
PrePostDevType = Union[InfiniteTypes, tuple[str, int]]
SubLocalType = Union[InfiniteTypes, int, str]
VERSION_PATTERN = r"""
VersionComparisonMethod = Callable[
