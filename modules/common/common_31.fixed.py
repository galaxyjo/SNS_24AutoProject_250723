
mv[:1] = b"\xff"
                self.expected, out2
                self.expected.decode(), out2
                self.expected.decode(), out3
            "Cryptodome.Hash.MD5",
            "Cryptodome.Hash.SHA1",
            # Data can be a memoryview (during initialization)
            # Data can be a memoryview (during operation)
            # Verify that both can reach the same state
            # Verify that changing the copy does not change the original
            (key, data, results, description, params) = list(row) + [{}]
            (key, data, results, description, params) = row
            )  # h = .new(); h.update(data); h.hexdigest()
            )  # h = .new(data); h.hexdigest()
            description = repr(input)
            description = row[2]
            h = self.module.new(self.key, self.data, **self.params)
            h.update(b"bla")
            h1 = self.module.new(**self.extra_params)
            h1 = self.module.new(data, **self.extra_params)
            h1.update(data)
            h2 = h.copy()
            h2 = h.new()
            h2 = self.module.new(**self.extra_params)
            h2 = self.module.new(mv, **self.extra_params)
            h2.update(b"bla")
            h2.update(mv)
            h2.update(self.input)
            h3 = h.copy()
            if not mv.readonly:
            mv = get_mv(data)
            out5 = binascii.b2a_hex(h2.digest())
            pass
            return memoryview(bytearray(data))
            return memoryview(data)
            self.assertEqual(
            self.assertEqual(h.digest(), h2.digest())
            self.assertEqual(h1.digest(), h2.digest())
            self.assertEqual(h3.digest(), self.result)
            self.assertEqual(self.expected, out3)  # h = .new(data); h.hexdigest()
            self.assertEqual(self.expected, out5)
            self.assertEqual(self.hashmod.digest_size, self.expected)
            self.assertTrue(hasattr(self.hashmod, "digest_size"))
        # Data can be a bytearray (during initialization)
        # Data can be a bytearray (during operation)
        # for MD5 and SHA1, which are hashlib objects.  (But test any .new()
        # method that does exist.)
        # PY3K: Check that .hexverify() accepts bytes or str
        # PY3K: Check that hexdigest() returns str and digest() returns bytes
        # PY3K: hexdigest() should return str(), and digest() bytes
        # Test .copy()
        # Verify again, with data passed to new()
        # Verify result
        # Verify that correct MAC does not raise any exception
        # Verify that incorrect MAC does raise ValueError exception
        # Verify that the .new() method produces a fresh hash object, except
        (expected, input) = map(tobytes, row[0:2])
        ) or hasattr(h, "new"):
        ba = bytearray(data)
        ba[:1] = b"\xff"
        data = b"\x00\x01\x02"
        data = b("\x00\x01\x02")
        def get_mv_ro(data):
        def get_mv_rw(data):
        else:
        except NotImplementedError:
        for get_mv in get_mv_ro, get_mv_rw:
        h = self.hashmod.new(**self.extra_params)
        h = self.hashmod.new(self.input, **self.extra_params)
        h = self.module.new(self.key, **self.params)
        h = self.module.new(self.key, self.data, **self.params)
        h.hexverify(h.hexdigest())
        h.hexverify(h.hexdigest().encode("ascii"))
        h.hexverify(result_hex)
        h.update(self.data)
        h.update(self.input)
        h.verify(self.result)
        h1 = self.module.new(**self.extra_params)
        h1 = self.module.new(data, **self.extra_params)
        h1.update(data)
        h2 = self.module.new(**self.extra_params)
        h2 = self.module.new(ba, **self.extra_params)
        h2.update(ba)
        if "truncate" not in self.extra_params:
        if len(row) < 3:
        if len(row) == 4:
        if self.hashmod.__name__ not in (
        if sys.version_info[0] == 2:
        name = "%s #%d: %s" % (module_name, i + 1, description)
        out1 = binascii.b2a_hex(h.digest())
        out2 = h.hexdigest()
        out3 = h.hexdigest()
        out4 = binascii.b2a_hex(h.digest())
        result_hex = hexlify(self.result)
        return self.description
        row = test_data[i]
        self.assertEqual(h.digest_size, self.expected)
        self.assertEqual(h.oid, self.oid)
        self.assertEqual(h1.digest(), h2.digest())
        self.assertEqual(hexlify(self.result).decode("ascii"), h.hexdigest())
        self.assertEqual(self.expected, out1)  # h = .new(); h.update(data); h.digest()
        self.assertEqual(self.expected, out4)  # h = .new(data); h.digest()
        self.assertEqual(self.result, h.digest())
        self.assertRaises(ValueError, h.hexverify, "4556")
        self.assertRaises(ValueError, h.verify, wrong_mac)
        self.assertTrue(hasattr(h, "digest_size"))
        self.assertTrue(isinstance(h.digest(), bytes))
        self.assertTrue(isinstance(h.hexdigest(), str))
        self.data = t2b(data)
        self.description = description
        self.expected = expected
        self.expected = expected.lower()
        self.extra_params = extra_params
        self.hashmod = hashmod
        self.input = input
        self.key = t2b(key)
        self.module = module
        self.oid = oid
        self.params = params
        self.result = t2b(result)
        tests.append(HashSelfTest(module, name, expected, input, extra_params))
        tests.append(HashTestOID(module, oid, extra_params))
        tests.append(MACSelfTest(module, name, results, data, key, params))
        try:
        unittest.TestCase.__init__(self)
        wrong_mac = strxor_c(self.result, 255)
    def __init__(self, *args, **kwargs): pass
    def __init__(self, hashmod, description, expected, extra_params):
    def __init__(self, hashmod, description, expected, input, extra_params):
    def __init__(self, hashmod, oid, extra_params):
    def __init__(self, module, description, result, data, key, params):
    def __init__(self, module, extra_params):
    def runTest(self):
    def shortDescription(self):
    for i in range(len(test_data)):
    for i, row in enumerate(test_data):
    if oid is not None:
    module, module_name, test_data, digest_size, oid=None, extra_params={}
    name = "%s #%d: digest_size" % (module_name, len(test_data) + 1)
    return tests
    return unhexlify(shorter)
    shorter = re.sub(rb"\s+", b"", tobytes(hex_string))
    tests = []
    tests.append(ByteArrayTest(module, extra_params))
    tests.append(HashDigestSizeSelfTest(module, name, digest_size, extra_params))
    tests.append(MemoryViewTest(module, extra_params))
"""Self-testing for PyCryptodome hash modules"""
#
#  SelfTest/Hash/common.py: Common code for Cryptodome.SelfTest.Hash
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
# vim:set ts=4 sw=4 sts=4 expandtab:
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
):
class ByteArrayTest:
class HashDigestSizeSelfTest:
class HashSelfTest:
class HashTestOID:
class MACSelfTest:
class MemoryViewTest:
def make_hash_tests(
def make_mac_tests(module, module_name, test_data):
def t2b(hex_string):
import binascii
import re
import sys
import unittest
from binascii import hexlify, unhexlify

from Cryptodome.Util.py3compat import b, tobytes
from Cryptodome.Util.strxor import strxor_c

pass
