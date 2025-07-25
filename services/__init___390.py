
    "compute_hash",
    "decrypt",
    "DecryptionError",
    "encrypt",
    "find_signature_hash",
    "newkeys",
    "PrivateKey",
    "PublicKey",
    "sign",
    "sign_hash",
    "VerificationError",
    "verify",
    compute_hash,
    decrypt,
    DecryptionError,
    doctest.testmod()
    encrypt,
    find_signature_hash,
    import doctest
    sign,
    sign_hash,
    VerificationError,
    verify,
"""
"""RSA module
#
#      https://www.apache.org/licenses/LICENSE-2.0
#  Copyright 2011 Sybren A. Stüvel <sybren@stuvel.eu>
#  distributed under the License is distributed on an "AS IS" BASIS,
#  Licensed under the Apache License, Version 2.0 (the "License");
#  limitations under the License.
#  See the License for the specific language governing permissions and
#  Unless required by applicable law or agreed to in writing, software
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# Do doctest if we're run directly
)
]
__all__ = [
__author__ = "Sybren Stuvel, Barry Mead and Yesudeep Mangalapilly"
__date__ = "2025-04-16"
__version__ = "4.9.1"
and verification. Includes generating public and private keys.
from rsa.key import newkeys, PrivateKey, PublicKey
from rsa.pkcs1 import (
if __name__ == "__main__":
Module for calculating large primes, and RSA encryption, decryption, signing
prevent repetitions, or other common security improvements. Use with care.
WARNING: this implementation does not use compression of the cleartext input to
