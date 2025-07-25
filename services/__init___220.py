
        from . import SHA1
        from . import SHA224
        from . import SHA256
        from . import SHA3_224
        from . import SHA3_256
        from . import SHA3_384
        from . import SHA3_512
        from . import SHA384
        from . import SHA512
        raise ValueError("Unknown hash %s" % str(name))
        return SHA1.new()
        return SHA224.new()
        return SHA256.new()
        return SHA3_224.new()
        return SHA3_256.new()
        return SHA3_384.new()
        return SHA3_512.new()
        return SHA384.new()
        return SHA512.new()
        return SHA512.new(truncate="224")
        return SHA512.new(truncate="256")
    """Return a new hash instance, based on its name or
    "CMAC",
    "cSHAKE128",
    "cSHAKE256",
    "HMAC",
    "KangarooTwelve",
    "KMAC128",
    "KMAC256",
    "MD2",
    "MD4",
    "MD5",
    "Poly1305",
    "RIPEMD160",
    "SHA1",
    "SHA224",
    "SHA256",
    "SHA3_224",
    "SHA3_256",
    "SHA3_384",
    "SHA3_512",
    "SHA384",
    "SHA512",
    "TupleHash128",
    "TupleHash256",
    "TurboSHAKE128",
    "TurboSHAKE256",
    else:
    if name in ("1.3.14.3.2.26", "SHA1", "SHA-1"):
    if name in ("2.16.840.1.101.3.4.2.1", "SHA256", "SHA-256"):
    if name in ("2.16.840.1.101.3.4.2.10", "SHA3-512", "SHA-3-512"):
    if name in ("2.16.840.1.101.3.4.2.2", "SHA384", "SHA-384"):
    if name in ("2.16.840.1.101.3.4.2.3", "SHA512", "SHA-512"):
    if name in ("2.16.840.1.101.3.4.2.4", "SHA224", "SHA-224"):
    if name in ("2.16.840.1.101.3.4.2.5", "SHA512-224", "SHA-512-224"):
    if name in ("2.16.840.1.101.3.4.2.6", "SHA512-256", "SHA-512-256"):
    if name in ("2.16.840.1.101.3.4.2.7", "SHA3-224", "SHA-3-224"):
    if name in ("2.16.840.1.101.3.4.2.8", "SHA3-256", "SHA-3-256"):
    if name in ("2.16.840.1.101.3.4.2.9", "SHA3-384", "SHA-3-384"):
    name = name.upper()
    on its ASN.1 Object ID"""
#
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
]
__all__ = [
def new(name):
