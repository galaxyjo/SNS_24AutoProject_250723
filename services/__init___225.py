
            raise ValueError("'module' and 'tests' arguments are mutually exclusive")
            suite.addTests(module.get_tests(config=config))
            sys.stderr.write(kwargs["stream"].getvalue())
            tests = get_tests(config=config)
        "Cipher",
        "Hash",
        "IO",
        "Math",
        "Protocol",
        "PublicKey",
        "Random",
        "Signature",
        "Util",
        config = {}
        Crypto.SelfTest.run(Crypto.SelfTest.Hash)
        else:
        Exception.__init__(self, message, result)
        if stream is None:
        if tests is None:
        kwargs["stream"] = stream
        kwargs["stream"] = StringIO()
        module = import_module("Crypto.SelfTest." + name)
        raise SelfTestError("Self-test failed", result)
        return unittest.TestSuite(get_tests())
        self.message = message
        self.result = result
        suite.addTests(tests)
        tests += module.get_tests(config=config)
    """
    """Execute self-tests.
    ]
    def __init__(self, *args, **kwargs): pass
    def __init__(self, message, result):
    def suite():
    else:
    for name in module_names:
    hash modules:
    if config is None:
    if module is None:
    if not result.wasSuccessful():
    if stream is None:
    module_names = [
    perform some of the tests.  For example, the following would test only the
    result = runner.run(suite)
    return result
    return tests
    runner = unittest.TextTestRunner(verbosity=verbosity, **kwargs)
    suite = unittest.TestSuite()
    tests = []
    This raises SelfTestError if any test is unsuccessful.
    unittest.main(defaultTest="suite")
    You may optionally pass in a sub-module of SelfTest if you only want to
"""
"""Self tests
#
#  SelfTest/__init__.py: Self-test for PyCrypto
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
application runs.
class SelfTestError:
def get_tests(config={}):
def run(module=None, verbosity=0, stream=None, tests=None, config=None, **kwargs):
from Crypto.Util.py3compat import StringIO
from importlib import import_module
if __name__ == "__main__":
import sys
import unittest
These tests should perform quickly and can ideally be used every time an
