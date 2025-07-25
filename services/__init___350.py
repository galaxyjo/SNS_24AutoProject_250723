
        from ._cmsgpack import Packer, unpackb
        from .fallback import Packer, unpackb
    """
    data = stream.read()
    except ImportError:
    from .fallback import Packer, unpackb
    Pack object `o` and return packed bytes
    Pack object `o` and write it to `stream`
    packer = Packer(**kwargs)
    Raises `ExtraData` when `stream` contains extra bytes.
    return Packer(**kwargs).pack(o)
    return unpackb(data, **kwargs)
    See :class:`Packer` for options.
    See :class:`Unpacker` for options.
    stream.write(packer.pack(o))
    try:
    Unpack an object from `stream`.
# alias for compatibility to simplejson/marshal/pickle.
__version__ = "1.0.5"
def pack(o, stream, **kwargs):
def packb(o, **kwargs):
def unpack(stream, **kwargs):
dump = pack
dumps = packb
else:
if os.environ.get("MSGPACK_PUREPYTHON") or sys.version_info[0] == 2:
import os
import sys
load = unpack
loads = unpackb
version = (1, 0, 5)
