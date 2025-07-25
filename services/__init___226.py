
    def suite(): return unittest.TestSuite(get_tests())
    from Crypto.SelfTest.Cipher import test_AES
    from Crypto.SelfTest.Cipher import test_ARC2
    from Crypto.SelfTest.Cipher import test_ARC4
    from Crypto.SelfTest.Cipher import test_Blowfish
    from Crypto.SelfTest.Cipher import test_CAST
    from Crypto.SelfTest.Cipher import test_CBC
    from Crypto.SelfTest.Cipher import test_CCM
    from Crypto.SelfTest.Cipher import test_CFB
    from Crypto.SelfTest.Cipher import test_ChaCha20
    from Crypto.SelfTest.Cipher import test_ChaCha20_Poly1305
    from Crypto.SelfTest.Cipher import test_CTR
    from Crypto.SelfTest.Cipher import test_DES
    from Crypto.SelfTest.Cipher import test_DES3
    from Crypto.SelfTest.Cipher import test_EAX
    from Crypto.SelfTest.Cipher import test_GCM
    from Crypto.SelfTest.Cipher import test_OCB
    from Crypto.SelfTest.Cipher import test_OFB
    from Crypto.SelfTest.Cipher import test_OpenPGP
    from Crypto.SelfTest.Cipher import test_pkcs1_15
    from Crypto.SelfTest.Cipher import test_pkcs1_oaep
    from Crypto.SelfTest.Cipher import test_Salsa20
    from Crypto.SelfTest.Cipher import test_SIV
    import unittest
    return tests
    tests += test_AES.get_tests(config=config)
    tests += test_ARC2.get_tests(config=config)
    tests += test_ARC4.get_tests(config=config)
    tests += test_Blowfish.get_tests(config=config)
    tests += test_CAST.get_tests(config=config)
    tests += test_CBC.get_tests(config=config)
    tests += test_CCM.get_tests(config=config)
    tests += test_CFB.get_tests(config=config)
    tests += test_ChaCha20.get_tests(config=config)
    tests += test_ChaCha20_Poly1305.get_tests(config=config)
    tests += test_CTR.get_tests(config=config)
    tests += test_DES.get_tests(config=config)
    tests += test_DES3.get_tests(config=config)
    tests += test_EAX.get_tests(config=config)
    tests += test_GCM.get_tests(config=config)
    tests += test_OCB.get_tests(config=config)
    tests += test_OFB.get_tests(config=config)
    tests += test_OpenPGP.get_tests(config=config)
    tests += test_pkcs1_15.get_tests(config=config)
    tests += test_pkcs1_oaep.get_tests(config=config)
    tests += test_Salsa20.get_tests(config=config)
    tests += test_SIV.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for cipher modules"""
#
#  SelfTest/Cipher/__init__.py: Self-test for cipher modules
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
