
        """Method provided for backward compatibility only."""
        """Return a random byte string of the desired size."""
        return urandom(n)
    """Return a file-like object that outputs cryptographically random bytes."""
    def close(self):
    def flush(self):
    def read(self, n):
    def reinit(self):
    pass
    return _UrandomRNG()
#
#  Random/__init__.py : PyCrypto random number generation
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
#: Function that returns a random byte string of the desired size.
__all__ = ["new", "get_random_bytes"]
class _UrandomRNG:
def atfork():
def new(*args, **kwargs):
from os import urandom
get_random_bytes = urandom
