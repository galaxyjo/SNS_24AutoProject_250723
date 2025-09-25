# modules/common/common_31.py

import binascii
import re
import sys
import unittest
from binascii import hexlify, unhexlify
from Cryptodome.Util.py3compat import b, tobytes
from Cryptodome.Util.strxor import strxor_c

class ByteArrayTest: pass
class HashDigestSizeSelfTest: pass
class HashSelfTest: pass
class HashTestOID: pass
class MACSelfTest: pass
class MemoryViewTest: pass

def t2b(hex_string):
    return binascii.unhexlify(re.sub(rb"\s+", b"", tobytes(hex_string)))

def make_hash_tests(): pass
def make_mac_tests(module, module_name, test_data): pass
