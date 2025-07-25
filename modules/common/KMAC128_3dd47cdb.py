
                has been tampered with or that the MAC key is incorrect.
            authenticate.
            data (bytes/bytearray/memoryview): The next chunk of the message to
            Default is 64. Minimum is 8.
            hex_mac_tag (string): the expected MAC of the message, as a hexadecimal string.
            It is equivalent to an early call to :meth:`KMAC_Hash.update`.
            It must be at least 128 bits long (16 bytes).
            kwargs["mac_len"] = self.digest_size
            Optional. A customization byte string (``S`` in SP 800-185).
            Optional. The size of the authentication tag, in bytes.
            Optional. The very first chunk of the message to authenticate.
            raise TypeError("You can only call 'digest' or 'hexdigest' on this object")
            raise ValueError("MAC check failed")
            self._cshake.update(_right_encode(self.digest_size * 8))
            self._cshake.update(data)
            self._mac = self._cshake.read(self.digest_size)
            The key to use to compute the MAC.
            ValueError: if the MAC does not match. It means that the message
          mac_tag (bytes/bytearray/memoryview): the expected MAC of the message.
        """
        """Authenticate the next chunk of message.
        """Return a new instance of a KMAC hash object.
        """Return the **binary** (non-printable) MAC tag of the message.
        """Return the **printable** MAC tag of the message.
        """Verify that a given **binary** MAC (computed by another party)
        """Verify that a given **printable** MAC (computed by another party)
        # See https://tools.ietf.org/html/rfc8702
        :return: The MAC tag. Binary form.
        :return: The MAC tag. Hexadecimal encoded.
        :rtype: byte string
        :rtype: string
        A :class:`KMAC_Hash` hash object
        Args:
        custom (bytes/bytearray/memoryview):
        data (bytes/bytearray/memoryview):
        if "mac_len" not in kwargs:
        if data:
        if mac1.digest() != mac2.digest():
        if not self._mac:
        if self._mac:
        is valid.
        key (bytes/bytearray/memoryview):
        mac_len (integer):
        mac1 = SHA3_256.new(secret + mac_tag)
        mac2 = SHA3_256.new(secret + self.digest())
        partial_newX = _bytepad(_encode_str(tobytes(key)), rate)
        raise TypeError("Unknown parameters: " + str(kwargs))
        raise TypeError("You must pass a key to KMAC128")
        raise ValueError("'mac_len' must be 8 bytes or more")
        raise ValueError("The key must be at least 128 bits long (16 bytes)")
        Raises:
        return "".join(["%02x" % bord(x) for x in tuple(self.digest())])
        return new(**kwargs)
        return self
        return self._mac
        secret = get_random_bytes(16)
        See :func:`new`.
        self._cshake = cshake._new(partial_newX, custom, b"KMAC")
        self._cshake.update(data)
        self._mac = None
        self.digest_size = mac_len
        self.oid = "2.16.840.1.101.3.4.2." + oid_variant
        self.verify(unhexlify(tobytes(hex_mac_tag)))
    """
    """A KMAC hash object.
    """Create a new KMAC128 object.
    Args:
    custom = kwargs.pop("custom", b"")
    data = kwargs.pop("data", None)
    def __init__(self, data, key, mac_len, custom, oid_variant, cshake, rate):
    def digest(self):
    def hexdigest(self):
    def hexverify(self, hex_mac_tag):
    def new(self, **kwargs):
    def update(self, data):
    def verify(self, mac_tag):
    Do not instantiate directly.
    if kwargs:
    if len(key) < 16:
    if mac_len < 8:
    if not is_bytes(key):
    key = kwargs.pop("key", None)
    mac_len = kwargs.pop("mac_len", 64)
    return KMAC_Hash(data, key, mac_len, custom, "19", cSHAKE128, 168)
    Returns:
    Use the :func:`new` function.
#
#    distribution.
#    notice, this list of conditions and the following disclaimer in
#    notice, this list of conditions and the following disclaimer.
#    the documentation and/or other materials provided with the
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# -*- coding: utf-8 -*-
# ===================================================================
# 1. Redistributions of source code must retain the above copyright
# 2. Redistributions in binary form must reproduce the above copyright
# All rights reserved.
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# are met:
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# Copyright (c) 2021, Legrandin <helderijs@gmail.com>
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# modification, are permitted provided that the following conditions
# POSSIBILITY OF SUCH DAMAGE.
# Redistribution and use in source and binary forms, with or without
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
class KMAC_Hash:
def new(**kwargs):
from . import cSHAKE128, SHA3_256
from .cSHAKE128 import _bytepad, _encode_str, _right_encode
from binascii import unhexlify
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.py3compat import bord, tobytes, is_bytes
