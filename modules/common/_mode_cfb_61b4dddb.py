
                                            const uint8_t iv[],
                                            size_t iv_len,
                                            size_t segment_len, /* In bytes */
                                            void **pResult);
                                    const uint8_t *in,
                                    size_t data_len);
                                    uint8_t *out,
                    "  (%d bytes)" % len(plaintext)
                    "output must have the same length as the input"
                    int CFB_decrypt(void *cfbState,
                    int CFB_encrypt(void *cfbState,
                    int CFB_start_operation(void *cipher,
                    int CFB_stop_operation(void *state);""",
                )
                raise TypeError("output must be a bytearray or a writeable memoryview")
                raise ValueError(
             >>> c.decrypt(a+b)
             >>> c.encrypt(a+b)
            "Incorrect IV length (it must be %d bytes long)" % factory.block_size
            **The IV must be unpredictable**. Ideally it is picked randomly.
            >>> c.decrypt(a) + c.decrypt(b)
            >>> c.encrypt(a) + c.encrypt(b)
            A smart pointer to the low-level block cipher instance.
            block_cipher.get(),
            c_size_t(len(ciphertext)),
            c_size_t(len(iv)),
            c_size_t(len(plaintext)),
            c_size_t(segment_size),
            c_uint8_ptr(ciphertext),
            c_uint8_ptr(iv),
            c_uint8_ptr(plaintext),
            ciphertext = create_string_buffer(len(plaintext))
            ciphertext = output
            compromises confidentiality.
            If ``None``, the ciphertext is returned.
            If ``None``, the plaintext is returned.
            if len(ciphertext) != len(output):
            if len(plaintext) != len(output):
            if not is_writeable_buffer(output):
            It can be of any length.
            It is as long as the cipher block.
            plaintext = create_string_buffer(len(ciphertext))
            plaintext = output
            raise TypeError("decrypt() cannot be called after encrypt()")
            raise TypeError("encrypt() cannot be called after decrypt()")
            raise TypeError("You must either use 'iv' or 'IV', not both")
            raise ValueError("Error %d while decrypting in CFB mode" % result)
            raise ValueError("Error %d while encrypting in CFB mode" % result)
            raise ValueError("Error %d while instantiating the CFB mode" % result)
            return get_raw_buffer(ciphertext)
            return get_raw_buffer(plaintext)
            return None
            Reusing the *IV* for encryptions performed with the same key
            self._state.address_of(),
            self._state.get(),
            The initialization vector to use for encryption or decryption.
            The location where the ciphertext must be written to.
            The location where the plaintext must be written to.
            The number of bytes the plaintext and ciphertext are segmented in.
            The piece of data to decrypt.
            The piece of data to encrypt.
          block_cipher : C pointer
          ciphertext : bytes/bytearray/memoryview
          If ``output`` is ``None``, the ciphertext is returned as ``bytes``.
          If ``output`` is ``None``, the plaintext is returned as ``bytes``.
          iv : bytes/bytearray/memoryview
          Otherwise, ``None``.
          output : bytearray/memoryview
          plaintext : bytes/bytearray/memoryview
          segment_size : integer
        """
        """Alias for `iv`"""
        """Create a new block cipher, configured in CFB mode.
        """Decrypt data with the key and the parameters set at initialization.
        """Encrypt data with the key and the parameters set at initialization.
        """The block size of the underlying cipher, in bytes."""
        """The Initialization Vector originally used to create the object.
        # by the cipher mode
        # Ensure that object disposal of this Python object will (eventually)
        # free the memory allocated by the raw library for the cipher mode
        # Memory allocated for the underlying block cipher is now owed
        )
        :Keywords:
        :Parameters:
        :Return:
        A cipher object is stateful: once you have decrypted a message
        A cipher object is stateful: once you have encrypted a message
        Alias for ``iv``.
        block_cipher.release()
        else:
        if "decrypt" not in self._next:
        if "encrypt" not in self._next:
        if IV is not None:
        If not present, the default is 8.
        if output is None:
        if result:
        is equivalent to:
        iv = get_random_bytes(factory.block_size)
        iv = IV
        more pieces and `decrypt` can be called multiple times.
        more pieces and `encrypt` can be called multiple times.
        object.
        raise TypeError("Unknown parameters for CFB: %s" % str(kwargs))
        raise ValueError(
        raise ValueError("'segment_size' must be positive and multiple of 8 bits")
        result = raw_cfb_lib.CFB_decrypt(
        result = raw_cfb_lib.CFB_encrypt(
        result = raw_cfb_lib.CFB_start_operation(
        self._next = ["decrypt"]
        self._next = ["encrypt", "decrypt"]
        self._next = ["encrypt"]
        self._state = SmartPointer(self._state.get(), raw_cfb_lib.CFB_stop_operation)
        self._state = VoidPointer()
        self.block_size = len(iv)
        self.iv = _copy_bytes(None, None, iv)
        self.IV = self.iv
        That is, the statement:
        The data to decrypt can be broken up in two or
        The data to encrypt can be broken up in two or
        The IV to use for CFB.
        The number of bit the plaintext and ciphertext are segmented in.
        The underlying block cipher, a module from ``Cryptodome.Cipher``.
        The value does not change."""
        This function does not add any padding to the plaintext.
        This function does not remove any padding from the plaintext.
        you cannot decrypt (or encrypt) another message with the same
        you cannot encrypt (or decrypt) another message using the same
      factory : module
      IV : bytes/bytearray/memoryview
      iv : bytes/bytearray/memoryview
      segment_size : integer
    """
    """*Cipher FeedBack (CFB)*.
    """Instantiate a cipher object that performs CFB encryption/decryption.
    "Cryptodome.Cipher._raw_cfb",
    .. _`NIST SP800-38A` : http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
    :Keywords:
    :Parameters:
    :undocumented: __init__
    An Initialization Vector (*IV*) is required.
    Any other keyword will be passed to the underlying block cipher.
    c_size_t,
    c_uint8_ptr,
    cipher_state = factory._create_base_cipher(kwargs)
    create_string_buffer,
    def __init__(self, block_cipher, iv, segment_size):
    def decrypt(self, ciphertext, output=None):
    def encrypt(self, plaintext, output=None):
    else:
    get_raw_buffer,
    if (None, None) == (iv, IV):
    if iv is not None:
    if kwargs:
    if len(iv) != factory.block_size:
    if segment_size_bytes == 0 or rem != 0:
    is_writeable_buffer,
    IV = kwargs.pop("iv", None)
    iv = kwargs.pop("IV", None)
    labelled **s**-bit CFB.
    load_pycryptodome_raw_lib,
    of **s** bits. The mode is therefore sometimes
    Plaintext and ciphertext are processed in *segments*
    return CfbMode(cipher_state, iv, segment_size_bytes)
    See `NIST SP800-38A`_ , Section 6.3.
    See the relevant documentation for details (at least ``key`` will need
    segment_size_bytes, rem = divmod(kwargs.pop("segment_size", 8), 8)
    SmartPointer,
    the underlying block cipher into a stream cipher.
    This mode is similar to CFB, but it transforms
    to be present).
    VoidPointer,
"""
#
#  Cipher/mode_cfb.py : CFB mode
# -*- coding: utf-8 -*-
# ===================================================================
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# contents of this file for any purpose whatsoever.
# everyone is granted a worldwide, perpetual, royalty-free,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# No rights are reserved.
# non-exclusive license to exercise all rights associated with the
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# SOFTWARE.
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
)
__all__ = ["CfbMode"]
class CfbMode:
Counter Feedback (CFB) mode.
def _create_cfb_cipher(factory, **kwargs):
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util._raw_api import (
from Cryptodome.Util.py3compat import _copy_bytes
raw_cfb_lib = load_pycryptodome_raw_lib(
