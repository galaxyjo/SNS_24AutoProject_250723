
                "empty range for randrange({!r}, {!r}, {!r})".format(start, stop, step)
                "randrange expected at most 3 arguments, got %d" % (len(args),)
                r = self.randrange(num_choices)
            (start, stop) = args
            (start, stop, step) = args
            (stop,) = args
            )
            j = self.randrange(0, i + 1)  # choose random j such that 0 <= j <= i
            not is_native_int(start)
            num_choices = 0
            or not is_native_int(step)
            or not is_native_int(stop)
            r = None
            r = self.getrandbits(size(num_choices))
            raise IndexError("empty sequence")
            raise TypeError(
            raise TypeError("randint requires integer arguments")
            raise TypeError("randrange requires integer arguments")
            raise ValueError(
            raise ValueError("Cannot specify both 'rng' and 'randfunc'")
            raise ValueError("randrange step argument must not be zero")
            raise ValueError("sample larger than population")
            retval.append(population[r])
            selected[r] = 1
            self._randfunc = None
            self._randfunc = randfunc
            self._randfunc = Random.new().read
            self._randfunc = rng.read
            start = 0
            step = 1
            while r is None or r in selected:
            x[i], x[j] = x[j], x[i]  # exchange x[i] and x[j]
        """
        """randrange([start,] stop[, step]):
        """Return a k-length list of unique elements chosen from the population sequence."""
        """Return a random element from a (non-empty) sequence.
        """Return a random integer N such that a <= N <= b."""
        """Return an integer with k random bits."""
        """Shuffle the sequence in place."""
        # Fisher-Yates shuffle.  O(n)
        # from the remaining items until all items have been chosen.
        # Pick a random number in the range of possible numbers
        # See http://en.wikipedia.org/wiki/Fisher-Yates_shuffle
        # Working backwards from the end of the array, we choose a random item
        ):
        assert a <= N <= b
        elif len(args) == 1:
        elif len(args) == 2:
        elif randfunc is None and rng is not None:
        elif randfunc is not None and rng is None:
        else:
        for i in range(k):
        for i in range(len(x) - 1, 0, -1):  # iterate from len(x)-1 downto 1
        if (
        if k > num_choices:
        if len(args) == 3:
        if len(seq) == 0:
        if not is_native_int(a) or not is_native_int(b):
        if num_choices < 0:
        if num_choices < 1:
        if randfunc is None and rng is None:
        if self._randfunc is None:
        if step == 0:
        If the seqence is empty, raises IndexError.
        mask = (1 << k) - 1
        N = self.randrange(a, b + 1)
        num_choices = ceil_div(stop - start, step)
        num_choices = len(population)
        r = num_choices
        Return a randomly-selected element from range(start, stop, step)."""
        return mask & bytes_to_long(self._randfunc(ceil_div(k, 8)))
        return N
        return retval
        return seq[self.randrange(len(seq))]
        return start + (step * r)
        retval = []
        selected = {}  # we emulate a set using a dict here
        while r >= num_choices:
    "choice",
    "getrandbits",
    "randint",
    "randrange",
    "sample",
    "shuffle",
    "StrongRandom",
    def __init__(self, rng=None, randfunc=None):
    def choice(self, seq):
    def getrandbits(self, k):
    def randint(self, a, b):
    def randrange(self, *args):
    def sample(self, population, k):
    def shuffle(self, x):
#
#  Random/random.py : Strong alternative for the standard 'random' module
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
# These are at the bottom to avoid problems with recursive imports
# vim:set ts=4 sw=4 sts=4 expandtab:
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
]
__all__ = [
_r = StrongRandom()
choice = _r.choice
class StrongRandom:
from Crypto.Util.number import ceil_div, bytes_to_long, size
from Crypto.Util.py3compat import is_native_int
getrandbits = _r.getrandbits
import Random
randint = _r.randint
randrange = _r.randrange
sample = _r.sample
shuffle = _r.shuffle
