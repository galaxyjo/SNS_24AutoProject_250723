
        return b("").join(s.split())
        return b("".join(s.split()))
    """
    """Convert binary to hexadecimal"""
    """Convert hexadecimal to binary, ignoring whitespace"""
    """Remove whitespace from a text or byte string"""
    """Return a list of TestCase instances given a TestCase class
    # For completeness
    else:
    if isinstance(s, str):
    return binascii.a2b_hex(strip_whitespace(s))
    return binascii.b2a_hex(s)
    return unittest.TestLoader().loadTestsFromTestCase(class_)
    This is useful when you have defined test* methods on your TestCase class.
"""Common functions for SelfTest modules"""
#
#  SelfTest/st_common.py: Common functions for SelfTest modules
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
# vim:set ts=4 sw=4 sts=4 expandtab:
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
def a2b_hex(s):
def b2a_hex(s):
def list_test_cases(class_):
def strip_whitespace(s):
from Crypto.Util.py3compat import b
import binascii
import unittest
