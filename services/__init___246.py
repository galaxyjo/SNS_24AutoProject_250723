
    def suite(): return unittest.TestSuite(get_tests())
    from Cryptodome.SelfTest.Hash import test_BLAKE2
    from Cryptodome.SelfTest.Hash import test_CMAC
    from Cryptodome.SelfTest.Hash import test_cSHAKE
    from Cryptodome.SelfTest.Hash import test_HMAC
    from Cryptodome.SelfTest.Hash import test_KangarooTwelve
    from Cryptodome.SelfTest.Hash import test_keccak
    from Cryptodome.SelfTest.Hash import test_KMAC
    from Cryptodome.SelfTest.Hash import test_MD2
    from Cryptodome.SelfTest.Hash import test_MD4
    from Cryptodome.SelfTest.Hash import test_MD5
    from Cryptodome.SelfTest.Hash import test_Poly1305
    from Cryptodome.SelfTest.Hash import test_RIPEMD160
    from Cryptodome.SelfTest.Hash import test_SHA1
    from Cryptodome.SelfTest.Hash import test_SHA224
    from Cryptodome.SelfTest.Hash import test_SHA256
    from Cryptodome.SelfTest.Hash import test_SHA3_224
    from Cryptodome.SelfTest.Hash import test_SHA3_256
    from Cryptodome.SelfTest.Hash import test_SHA3_384
    from Cryptodome.SelfTest.Hash import test_SHA3_512
    from Cryptodome.SelfTest.Hash import test_SHA384
    from Cryptodome.SelfTest.Hash import test_SHA512
    from Cryptodome.SelfTest.Hash import test_SHAKE
    from Cryptodome.SelfTest.Hash import test_TupleHash
    from Cryptodome.SelfTest.Hash import test_TurboSHAKE
    import unittest
    return tests
    tests += test_BLAKE2.get_tests(config=config)
    tests += test_CMAC.get_tests(config=config)
    tests += test_cSHAKE.get_tests(config=config)
    tests += test_HMAC.get_tests(config=config)
    tests += test_KangarooTwelve.get_tests(config=config)
    tests += test_keccak.get_tests(config=config)
    tests += test_KMAC.get_tests(config=config)
    tests += test_MD2.get_tests(config=config)
    tests += test_MD4.get_tests(config=config)
    tests += test_MD5.get_tests(config=config)
    tests += test_Poly1305.get_tests(config=config)
    tests += test_RIPEMD160.get_tests(config=config)
    tests += test_SHA1.get_tests(config=config)
    tests += test_SHA224.get_tests(config=config)
    tests += test_SHA256.get_tests(config=config)
    tests += test_SHA3_224.get_tests(config=config)
    tests += test_SHA3_256.get_tests(config=config)
    tests += test_SHA3_384.get_tests(config=config)
    tests += test_SHA3_512.get_tests(config=config)
    tests += test_SHA384.get_tests(config=config)
    tests += test_SHA512.get_tests(config=config)
    tests += test_SHAKE.get_tests(config=config)
    tests += test_TupleHash.get_tests(config=config)
    tests += test_TurboSHAKE.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for hash modules"""
#
#  SelfTest/Hash/__init__.py: Self-test for hash modules
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
__revision__ = "$Id$"
def get_tests(config={}):
if __name__ == "__main__":
