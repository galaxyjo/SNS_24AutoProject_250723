
                BlockSizeTest(module, params),
                ByteArrayTest(module, params),
                cipher.update(comp)
                decipher.update(comp)
                extra_params,
                IVLengthTest(module, params),
                NoDefaultECBTest(module, params),
                params["ciphertext"],
                params["description"],
                params["key"],
                params["plaintext"],
                RoundtripTest(module, params),
                self.assertEqual(ct, ctX)
                self.assertEqual(pt, ptX)
                self.iv = _extract(params, "nonce", None)
                self.iv = b(self.iv)
            # Block cipher
            # Only AEAD modes
            # Stream cipher
            (
            (params["plaintext"], params["ciphertext"], params["key"]) = row
            ) = row
            ]
            assoc_data = [a2b_hex(b(x)) for x in self.assoc_data]
            assoc_data = [bytearray(a2b_hex(b(x))) for x in self.assoc_data]
            assoc_data = [memoryview(a2b_hex(b(x))) for x in self.assoc_data]
            cipher = self._new()
            cipher.update(comp)
            ct, pt = ctX, ptX
            ct3.append(cipher.encrypt(plaintext[i: i + 3]))
            ctX = b2a_hex(cipher.encrypt(plaintext))
            decipher = self._new()
            decipher.update(comp)
            decipher.verify(a2b_hex(self.mac))
            decipher.verify(bytearray(a2b_hex(self.mac)))
            decipher.verify(memoryview(a2b_hex(self.mac)))
            desc += " in {} mode".format(self.mode_name)
            description = "p={}, k={}".format(p_plaintext, p_key)
            description = "p={}, k={}, {!r}".format(p_plaintext, p_key, p2)
            description = p_description
            extra_tests_added = True
            for comp in assoc_data:
            if ct:
            if self.iv is None:
            if self.iv is not None:
            mac = b2a_hex(cipher.digest())
            old_style += [a2b_hex(self.iv)]
            old_style = [self.mode]
            params.update(extra_params)
            params["mode"] = "ECB"
            pt3.append(cipher.encrypt(ciphertext[i: i + 3]))
            ptX = b2a_hex(decipher.decrypt(ciphertext))
            raise
            raise AssertionError("Unsupported tuple size %d" % (len(row),))
            return False
            self.assertEqual(self.mac, mac)
            self.iv = _extract(params, "iv", None)
            self.mac = b(self.mac)
            self.mode = getattr(self.module, "MODE_" + mode)
            self.mode = None
            self.module_name,
            tests += [
            tests.append(MemoryviewTest(module, params))
            TypeError, self.module.new, a2b_hex(self.key), self.module.MODE_ECB, b("")
        #
        # - (optionally) any other parameter that this cipher mode requires
        # - (optionally) description
        # - ciphertext
        # - key
        # - mode (default is ECB)
        # - plaintext
        # Add extra test(s) to the test suite before the current test
        # Add the current test to the test suite
        # Add the test to the test suite
        # Build the "params" dictionary
        # Build the "params" dictionary with
        # Build the display-name for the test
        # ECB mode
        # Extract the parameters
        # Only AEAD modes
        # PY3K: This is meant to be text, do not change to bytes (data)
        # Repeat the same encryption or decryption twice and verify
        # Test counter mode decryption, 3 bytes at a time
        # Test counter mode encryption, 3 bytes at a time
        # that the result is always the same
        # The cipher should work like a stream cipher
        )
        assoc_data = []
        cipher = self._new()
        cipher = self.module.new(self.key, self.module.MODE_ECB)
        ciphertext = a2b_hex(self.ciphertext)
        ciphertext = encryption_cipher.encrypt(self.plaintext)
        ct = b2a_hex(cipher.encrypt(bytearray(plaintext)))
        ct = b2a_hex(cipher.encrypt(memoryview(plaintext)))
        ct = None
        ct3 = []
        ct3 = b2a_hex(b("").join(ct3))
        decipher = self._new()
        decrypted_plaintext = decryption_cipher.decrypt(ciphertext)
        decryption_cipher = self.module.new(a2b_hex(self.key), mode)
        desc = self.module_name
        elif len(row) == 4:
        elif len(row) == 5:
        elif not p2:
        elif p_mode == "ECB" and not p2:
        else:
        encryption_cipher = self.module.new(a2b_hex(self.key), mode)
        for comp in assoc_data:
        for i in range(0, len(ciphertext), 3):
        for i in range(0, len(plaintext), 3):
        for i in range(2):
        from Crypto import Random
        if default is _NoDefault:
        if len(row) == 3:
        if mode is not None:
        if not "mode" in params:
        if not extra_tests_added:
        if not hasattr(self.module, "MODE_" + name):
        if p_description is not None:
        if self.assoc_data:
        if self.iv is not None:
        if self.mac:
        if self.mode is not None:
        key = a2b_hex(self.key)
        mode = _extract(params, "mode", None)
        mode = self.module.MODE_ECB
        name = "%s #%d: %s" % (module_name, i + 1, description)
        old_style = []
        p_ciphertext = _extract(p2, "ciphertext")
        p_description = _extract(p2, "description", None)
        p_key = _extract(p2, "key")
        p_mode = _extract(p2, "mode")
        p_plaintext = _extract(p2, "plaintext")
        p2 = params.copy()
        params = {}
        params = params.copy()
        params = self.extra_params.copy()
        params.update(additional_params)
        params["description"] = name
        params["module_name"] = module_name
        plaintext = a2b_hex(self.plaintext)
        pt = b2a_hex(decipher.decrypt(bytearray(ciphertext)))
        pt = b2a_hex(decipher.decrypt(memoryview(ciphertext)))
        pt = None
        pt3 = []
        pt3 = b2a_hex(b("").join(pt3))
        return """{} .decrypt() output of .encrypt() should not be garbled""".format(
        return "{} should behave like a stream cipher".format(desc)
        return "\0" * self.module.block_size
        return "Check that all modes except MODE_ECB and MODE_CTR require an IV of the proper length"
        return default
        return self.description
        return self.mode == getattr(self.module, "MODE_" + name)
        return self.module.new(key, *old_style, **params)
        retval = d[k]
        row = test_data[i]
        self.assertEqual(cipher.block_size, self.module.block_size)
        self.assertEqual(self.ciphertext, ct)  # encrypt
        self.assertEqual(self.ciphertext, ct3)  # encryption (3 bytes at a time)
        self.assertEqual(self.plaintext, decrypted_plaintext)
        self.assertEqual(self.plaintext, pt)  # decrypt
        self.assertEqual(self.plaintext, pt3)  # decryption (3 bytes at a time)
        self.assertRaises(
        self.assertRaises(TypeError, self.module.new, a2b_hex(self.key))
        self.assoc_data = _extract(params, "assoc_data", None)
        self.ciphertext = b(_extract(params, "ciphertext"))
        self.description = _extract(params, "description")
        self.extra_params = params
        self.iv = Random.get_random_bytes(module.block_size)
        self.key = a2b_hex(b(params["key"]))
        self.key = b(_extract(params, "key"))
        self.key = b(params["key"])
        self.mac = _extract(params, "mac", None)
        self.mode_name = str(mode)
        self.module = module
        self.module_name = _extract(params, "module_name", None)
        self.module_name = params.get("module_name", None)
        self.plaintext = 100 * b(params["plaintext"])
        self.plaintext = b(_extract(params, "plaintext"))
        tests.append(CipherSelfTest(module, params))
        tests.append(CipherStreamingSelfTest(module, params))
        unittest.TestCase.__init__(self)
    """Get an item from a dictionary, and remove it from the dictionary."""
    """Verify we can use bytearray's for encrypting and decrypting"""
    """Verify we can use memoryviews for encrypting and decrypting"""
    def __init__(self, *args, **kwargs): pass
    def __init__(self, module, params):
    def _dummy_counter(self):
    def _new(self):
    def isMode(self, name):
    def runTest(self):
    def shortDescription(self):
    del d[k]
    except KeyError:
    extra_tests_added = False
    for i in range(len(test_data)):
    pass  # sentinel object
    return retval
    return tests
    tests = []
    try:
"""Self-testing for PyCrypto hash modules"""
#
#  SelfTest/Hash/common.py: Common code for Crypto.SelfTest.Hash
# ===================================================================
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# contents of this file for any purpose whatsoever.
# everyone is granted a worldwide, perpetual, royalty-free,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# Generic cipher test case
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# No rights are reserved.
# non-exclusive license to exercise all rights associated with the
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# SOFTWARE.
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# vim:set ts=4 sw=4 sts=4 expandtab:
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
class _NoDefault:
class BlockSizeTest:
class ByteArrayTest:
class CipherSelfTest:
class CipherStreamingSelfTest:
class IVLengthTest:
class MemoryviewTest:
class NoDefaultECBTest:
class RoundtripTest:
def _extract(d, k, default=_NoDefault):
def make_block_tests(module, module_name, test_data, additional_params=dict()):
def make_stream_tests(module, module_name, test_data):
from binascii import a2b_hex, b2a_hex
from Crypto.Util.py3compat import b
import unittest
