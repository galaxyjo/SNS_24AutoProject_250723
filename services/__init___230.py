
        from Crypto.SelfTest.Protocol import test_HPKE
        tests += test_HPKE.get_tests(config=config)
    def suite(): return unittest.TestSuite(get_tests())
    from Crypto.SelfTest.Protocol import test_ecdh
    from Crypto.SelfTest.Protocol import test_KDF
    from Crypto.SelfTest.Protocol import test_rfc1751
    from Crypto.SelfTest.Protocol import test_SecretSharing
    if sys.version_info >= (3, 9):
    import unittest
    return tests
    tests += test_ecdh.get_tests(config=config)
    tests += test_KDF.get_tests(config=config)
    tests += test_rfc1751.get_tests(config=config)
    tests += test_SecretSharing.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for Crypto.Protocol"""
#
#  SelfTest/Protocol/__init__.py: Self-tests for Crypto.Protocol
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
def get_tests(config={}):
if __name__ == "__main__":
import sys
