
                encoding = self._fallback_encoding
                return ""
                self._buffer = input
            # Any python_name value that gets to here should be valid.
            assert decoder.encoding is not None
            break
            codec_info = codecs.lookup(python_name)
            else:  # No BOM
            from .x_user_defined import codec_info
            if len(input) < 3 and not final:  # Not enough data yet.
            Indicate that no more input is available.
            Must be :obj:`True` if this is the last call.
            python_name = PYTHON_NAMES.get(name, name)
            return decoder(input, final)
            yield decoder.encoding
            yield output
        """
        """Decode one chunk of the input.
        # Fail early if `encoding` is an invalid label.
        # Input exhausted without determining the encoding
        #: (Ie. if there is not enough input yet to determine
        #: if there is a BOM.)
        #: or :obj:`None` if that is not determined yet.
        #: The actual :class:`Encoding` that is being used,
        :obj:`encoding` is the :obj:`Encoding` that is being used.
        :obj:`output` is an iterable of Unicode strings,
        :param final:
        :param input: A byte string.
        :param input: An Unicode string.
        :returns: A byte string.
        :returns: An Unicode string.
        >>> assert ascii_lower(keyword) != keyword.lower()
        >>> assert ascii_lower(keyword) == u'bac\N{KELVIN SIGN}ground'
        >>> assert keyword.lower() == u'background'
        >>> keyword = u'Bac\N{KELVIN SIGN}ground'
        A ``(output, encoding)`` tuple of an Unicode string
        a stdlib :class:`~codecs.CodecInfo` object.
        An :class:`Encoding` object or a label string.
        An :class:`Encoding` object, or :obj:`None` for an unknown label.
        An ``(output, encoding)`` tuple.
        An iterable of byte strings.
        and an :obj:`Encoding`.
        assert decoder.encoding is not None
        based on the precense of a BOM,
        CACHE[name] = encoding
        Canonical name of the encoding
        decoder = encoding.codec_info.incrementaldecoder(self._errors).decode
        decoder = self._decoder
        else:
        encoding = _get_encoding(encoding)
        encoding = Encoding(name, codec_info)
        encoding, input = _detect_bom(input)
        if decoder is not None:
        if encoding is None:
        if name == "x-user-defined":
        if output:
        input = self._buffer + input
        output = decode(b"", final=True)
        output = decode(chunck)
        output = encode(chunck)
        raise LookupError("Unknown encoding label: %r" % encoding_or_label)
        return
        return "<Encoding %s>" % self.name
        return _UTF16BE, input[2:]
        return _UTF16LE, input[2:]
        return decoder(input, final)
        return encoding_or_label
        return None
        return UTF8, input[3:]
        See :func:`codecs.register`.
        self._buffer = b""
        self._decoder = decoder
        self._decoder = None
        self._errors = errors
        self._fallback_encoding = _get_encoding(fallback_encoding)
        self.codec_info = codec_info
        self.encode = encoding.codec_info.incrementalencoder(errors).encode
        self.encoding = encoding
        self.encoding = None  # Not known yet.
        self.name = name
        The actual implementation of the encoding,
        The encoding to use if :obj:`input` does note have a BOM.
        The input is first consumed just enough to determine the encoding
        then consumed on demand when the return value is.
        yield decoder.encoding
        yield output
    """
    """Reresents a character encoding such as UTF-8,
    """Return (bom_encoding, input), with any BOM removed from the input."""
    """Return a generator that first yields the :obj:`Encoding`,
    "iso-8859-8-i": "iso-8859-8",
    "macintosh": "mac-roman",
    "Pull"-based decoder.
    "windows-874": "cp874",
    "x-mac-cyrillic": "mac-cyrillic",
    # Fail early if `encoding` is an invalid label.
    # Only strip ASCII whitespace: U+0009, U+000A, U+000C, U+000D, and U+0020.
    # This turns out to be faster than unicode.translate()
    .. attribute:: codec_info
    .. attribute:: name
    .. method:: encode(input, final=False)
    :param encoding: An :class:`Encoding` object or a label string.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :param fallback_encoding:
    :param input:
    :param input: A byte string
    :param input: An iterable of Unicode strings.
    :param input: An Unicode string.
    :param label: A string.
    :param string: An Unicode string.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.
    :raises: :exc:`~exceptions.LookupError` for an unknown label.
    :return:
    :return: A byte string.
    :returns:
    :returns: A new Unicode string.
    :returns: An :class:`Encoding` object.
    :returns: An iterable of byte strings.
    “Pull”-based encoder.
    “Push”-based decoder.
    “Push”-based encoder.
    <http://encoding.spec.whatwg.org/#ascii-case-insensitive>`_
    <http://encoding.spec.whatwg.org/#concept-encoding-get>`_ algorithm.
    Accept either an encoding object or label.
    bom_encoding, input = _detect_bom(input)
    decode = decoder.decode
    Decode a single string.
    decoder = IncrementalDecoder(fallback_encoding, errors)
    def __init__(self, encoding=UTF8, errors="strict"):
    def __init__(self, fallback_encoding, errors="replace"):
    def __init__(self, name, codec_info):
    def __repr__(self):
    def decode(self, input, final=False):
    else:
    encode = IncrementalEncoder(encoding, errors).encode
    Encode a single string.
    encoding = bom_encoding or fallback_encoding
    encoding = CACHE.get(name)
    encoding = lookup(encoding_or_label)
    encoding = next(generator)
    fallback_encoding = _get_encoding(fallback_encoding)
    for `CSS keywords <http://dev.w3.org/csswg/css-values/#keywords>`_.
    for chunck in input:
    generator = _iter_decode_generator(input, decoder)
    if encoding is None:
    if hasattr(encoding_or_label, "codec_info"):
    if input.startswith(b"\xef\xbb\xbf"):
    if input.startswith(b"\xfe\xff"):
    if input.startswith(b"\xff\xfe"):
    if name is None:
    if output:
    input = iter(input)
    label = ascii_lower(label.strip("\t\n\f\r "))
    Look for an encoding by its label.
    matching of encoding labels.
    name = LABELS.get(label)
    output = decode(b"", final=True)
    output = encode("", final=True)
    r"""Transform (only) ASCII letters to lower case: A-Z is mapped to a-z.
    return _get_encoding(encoding).codec_info.encode(input, errors)[0]
    return _iter_encode_generator(input, encode)
    return encoding
    return encoding.codec_info.decode(input, errors)[0], encoding
    return generator, encoding
    return None, input
    return string.encode("utf8").lower().decode("utf8")
    sometimes mapping them into the ASCII range:
    Supported labels are listed there.
    that can be used for decoding or encoding.
    The same matching is also used, among other things,
    then yields output chukns as Unicode strings.
    This is different from the :meth:`~py:str.lower` method of Unicode strings
    This is the spec’s `get an encoding
    This is used for `ASCII case-insensitive
    which also affect non-ASCII characters,
"""
# Some names in Encoding are not valid Python aliases. Remap these.
#: The UTF-8 encoding. Should be used for new content and formats.
:copyright: Copyright 2012 by Simon Sapin
:license: BSD, see LICENSE for details.
_UTF16BE = lookup("utf-16be")
_UTF16LE = lookup("utf-16le")
}
~~~~~~~~~~~~
<http://encoding.spec.whatwg.org/>`. See README for details.
CACHE = {}
class Encoding:
class IncrementalDecoder:
class IncrementalEncoder:
def _detect_bom(input):
def _get_encoding(encoding_or_label):
def _iter_decode_generator(input, decoder):
def _iter_encode_generator(input, encode):
def ascii_lower(string):
def decode(input, fallback_encoding, errors="replace"):
def encode(input, encoding=UTF8, errors="strict"):
def iter_decode(input, fallback_encoding, errors="replace"):
def iter_encode(input, encoding=UTF8, errors="strict"):
def lookup(label):
from .labels import LABELS
import codecs
PYTHON_NAMES = {
This is a Python implementation of the `WHATWG Encoding standard
UTF8 = lookup("utf-8")
VERSION = "0.5.1"
webencodings
