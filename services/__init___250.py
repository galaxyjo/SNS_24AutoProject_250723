
        return unittest.TestSuite(get_tests())
    def suite():
    return tests
    test_DSA,
    test_ECC_Curve25519,
    test_ECC_Curve448,
    test_ECC_Ed25519,
    test_ECC_Ed448,
    test_ECC_NIST,
    test_ElGamal,
    test_import_Curve25519,
    test_import_Curve448,
    test_import_DSA,
    test_import_ECC,
    test_import_RSA,
    test_RSA,
    tests += test_DSA.get_tests(config=config)
    tests += test_ECC_Curve25519.get_tests(config=config)
    tests += test_ECC_Curve448.get_tests(config=config)
    tests += test_ECC_Ed25519.get_tests(config=config)
    tests += test_ECC_Ed448.get_tests(config=config)
    tests += test_ECC_NIST.get_tests(config=config)
    tests += test_ElGamal.get_tests(config=config)
    tests += test_import_Curve25519.get_tests(config=config)
    tests += test_import_Curve448.get_tests(config=config)
    tests += test_import_DSA.get_tests(config=config)
    tests += test_import_ECC.get_tests(config=config)
    tests += test_import_RSA.get_tests(config=config)
    tests += test_RSA.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for public-key crypto"""
#
#  SelfTest/PublicKey/__init__.py: Self-test for public key crypto
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
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
)
def get_tests(config={}):
from Cryptodome.SelfTest.PublicKey import (
if __name__ == "__main__":
import unittest
