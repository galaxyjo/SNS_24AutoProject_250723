
            algo_params = algo[1]
            algo_params = None
            DerNull().decode(algo[1])
            raise ValueError("Incorrect X.509 certificate version")
        # Version not present
        * Algorithm parameters (bytes or None)
        * encoded public key (bytes)
        * OID (string)
        algo_params = None
        algorithm = DerSequence([DerObjectId(algo_oid), params])
        algorithm = DerSequence([DerObjectId(algo_oid)])
        except:
        if version not in (2, 3):
        index = 6
        tbs_certificate[0] + 1
        try:
        version = 1
        version = DerInteger(explicit=0).decode(tbs_certificate[0]).value
    """
    """Extract subjectPublicKeyInfo from a DER X.509 certificate."""
    """Parse a SubjectPublicKeyInfo structure.
    #
    #   algorithm         AlgorithmIdentifier,
    #   algorithm   OBJECT IDENTIFIER,
    #   parameters  ANY DEFINED BY algorithm OPTIONAL
    #   subjectPublicKey  BIT STRING
    # }
    # AlgorithmIdentifier  ::=  SEQUENCE  {
    # SubjectPublicKeyInfo  ::=  SEQUENCE  {
    algo = DerSequence().decode(spki[0], nr_elements=(1, 2))
    algo_oid = DerObjectId().decode(algo[0])
    certificate = DerSequence().decode(x509_certificate, nr_elements=3)
    DerBitString,
    DerInteger,
    DerNull,
    DerObjectId,
    DerSequence,
    else:
    except TypeError:
    if len(algo) == 1:
    if params is None:
    index = 5
    It returns a triple with:
    return algo_oid.value, spk, algo_params
    return spki.encode()
    return tbs_certificate[index]
    spk = DerBitString().decode(spki[1]).value
    spki = DerSequence().decode(encoded, nr_elements=2)
    spki = DerSequence([algorithm, DerBitString(public_key)])
    tbs_certificate = DerSequence().decode(certificate[0], nr_elements=range(6, 11))
    try:
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
)
def _create_subject_public_key_info(algo_oid, public_key, params):
def _expand_subject_public_key_info(encoded):
def _extract_subject_public_key_info(x509_certificate):
from Cryptodome.Util.asn1 import (
