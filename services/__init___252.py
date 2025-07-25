
        return unittest.TestSuite(get_tests())
    def suite():
    return tests
    tests += test_dss.get_tests(config=config)
    tests += test_eddsa.get_tests(config=config)
    tests += test_pkcs1_15.get_tests(config=config)
    tests += test_pss.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for signature modules"""
#
#  SelfTest/Signature/__init__.py: Self-test for signature modules
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
def get_tests(config={}):
from . import test_pkcs1_15, test_pss, test_dss, test_eddsa
if __name__ == "__main__":
import unittest
