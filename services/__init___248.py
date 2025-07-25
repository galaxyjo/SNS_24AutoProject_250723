
    def suite(): return unittest.TestSuite(get_tests())
    from Cryptodome.SelfTest.Math import test_modexp
    from Cryptodome.SelfTest.Math import test_modmult
    from Cryptodome.SelfTest.Math import test_Numbers
    from Cryptodome.SelfTest.Math import test_Primality
    import unittest
    return tests
    tests += test_modexp.get_tests(config=config)
    tests += test_modmult.get_tests(config=config)
    tests += test_Numbers.get_tests(config=config)
    tests += test_Primality.get_tests(config=config)
    tests = []
    unittest.main(defaultTest="suite")
"""Self-test for Math"""
#
#    distribution.
#    notice, this list of conditions and the following disclaimer in
#    notice, this list of conditions and the following disclaimer.
#    the documentation and/or other materials provided with the
#  SelfTest/Math/__init__.py: Self-test for math module
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# ===================================================================
# 1. Redistributions of source code must retain the above copyright
# 2. Redistributions in binary form must reproduce the above copyright
# All rights reserved.
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# are met:
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# Copyright (c) 2014, Legrandin <helderijs@gmail.com>
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# modification, are permitted provided that the following conditions
# POSSIBILITY OF SUCH DAMAGE.
# Redistribution and use in source and binary forms, with or without
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
def get_tests(config={}):
if __name__ == "__main__":
