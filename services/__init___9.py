
                                  to their more modern equivalents?
                              ``UniversalDetector.MINIMUM_THRESHOLD``
                              in results.
                        "confidence": prober.get_confidence(),
                        "encoding": charset_name,
                        "language": prober.language,
                        charset_name.lower(), charset_name
                        lower_charset_name, charset_name
                    )
                    {
                    }
                    charset_name = detector.ISO_WIN_MAP.get(
                    charset_name = detector.LEGACY_MAP.get(
                # extra Windows-specific bytes
                # Rename legacy encodings with superset encodings if asked
                # Use Windows encoding name instead of ISO-8859 if we saw any
                )
                charset_name = prober.charset_name or ""
                f"Expected object of type bytes or bytearray, got: {type(byte_str)}"
                if lower_charset_name.startswith("iso-8859") and detector.has_win_bytes:
                if should_rename_legacy:
                lower_charset_name = charset_name.lower()
                probers.append(prober)
                probers.extend(p for p in prober.probers)
                results.append(
            )
            else:
            if ignore_threshold or prober.get_confidence() > detector.MINIMUM_THRESHOLD:
            if isinstance(prober, CharSetGroupProber):
            raise TypeError(
            return sorted(results, key=lambda result: -result["confidence"])
        byte_str = bytearray(byte_str)
        for prober in detector.charset_probers:
        for prober in probers:
        if len(results) > 0:
        if not isinstance(byte_str, bytes):
        probers: List[CharSetProber] = []
        results: List[ResultDict] = []
    """
    :param byte_str:          The byte sequence to examine.
    :param byte_str:     The byte sequence to examine.
    :param ignore_threshold:  Include encodings that are below
    :param should_rename_legacy:  Should we rename legacy encodings
    :type byte_str:           ``bytes`` or ``bytearray``
    :type byte_str:      ``bytes`` or ``bytearray``
    :type ignore_threshold:   ``bool``
    :type should_rename_legacy:   ``bool``
    byte_str: Union[bytes, bytearray],
    byte_str: Union[bytes, bytearray], should_rename_legacy: bool = False
    Detect all the possible encodings of the given byte string.
    Detect the encoding of the given byte string.
    detector = UniversalDetector(should_rename_legacy=should_rename_legacy)
    detector.close()
    detector.feed(byte_str)
    if detector.input_state == InputState.HIGH_BYTE:
    if not isinstance(byte_str, bytearray):
    ignore_threshold: bool = False,
    return [detector.result]
    return detector.close()
    should_rename_legacy: bool = False,
#
# 02110-1301  USA
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# Lesser General Public License for more details.
# License along with this library; if not, write to the Free Software
# License as published by the Free Software Foundation; either
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# modify it under the terms of the GNU Lesser General Public
# This library is distributed in the hope that it will be useful,
# This library is free software; you can redistribute it and/or
# version 2.1 of the License, or (at your option) any later version.
# You should have received a copy of the GNU Lesser General Public
######################## BEGIN LICENSE BLOCK ########################
######################### END LICENSE BLOCK #########################
) -> List[ResultDict]:
) -> ResultDict:
__all__ = ["UniversalDetector", "detect", "detect_all", "__version__", "VERSION"]
def detect(
def detect_all(
from .charsetgroupprober import CharSetGroupProber
from .charsetprober import CharSetProber
from .enums import InputState
from .resultdict import ResultDict
from .universaldetector import UniversalDetector
from .version import VERSION, __version__
from typing import List, Union
