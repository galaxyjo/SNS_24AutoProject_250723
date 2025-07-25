
    def suite(): return unittest.TestSuite(get_tests())
    from Crypto.SelfTest.Util import test_asn1
    from Crypto.SelfTest.Util import test_Counter
    from Crypto.SelfTest.Util import test_number
    from Crypto.SelfTest.Util import test_Padding
    from Crypto.SelfTest.Util import test_rfc1751
    from Crypto.SelfTest.Util import test_strxor
    import unittest
    return tests
    tests += test_asn1.get_tests(config=config)
    tests += test_Counter.get_tests(config=config)
    tests += test_number.get_tests(config=config)
    tests += test_Padding.get_tests(config=config)
    tests += test_rfc1751.get_tests(config=config)
    tests += test_strxor.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for utility modules"""
#
#  SelfTest/Util/__init__.py: Self-test for utility modules
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
