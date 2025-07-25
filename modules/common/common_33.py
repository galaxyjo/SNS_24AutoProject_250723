
            "bit_size(num) only supports integers, not %r" % type(num)
            msg or "%d and %d are not relatively prime, divider=%i" % (a, b, d)
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
        )
        ) from ex
        >>> bit_size(1023)
        >>> bit_size(1024)
        >>> bit_size(1025)
        >>> byte_size((1 << 1024) - 1)
        >>> byte_size(1 << 1023)
        >>> byte_size(1 << 1024)
        >>> ceil_div(1, 4)
        >>> ceil_div(100, 10)
        >>> ceil_div(100, 7)
        1
        10
        11
        128
        129
        15
        An unsigned integer
        before the number's bit length is determined.
        Integer value. If num is 0, returns 0. Only the absolute value of the
        inv = inverse(M_i, m_i)
        lx += ob  # If neg wrap modulo original b
        ly += oa  # If neg wrap modulo original a
        m *= modulo
        M_i = m // m_i
        number is considered. Therefore, signed integers will be abs(num)
        q = a // b
        quanta += 1
        raise NotRelativePrimeError(x, n, divider)
        raise TypeError(
        return 1
        return num.bit_length()
        Returns the number of bits in the integer.
        self.a = a
        self.b = b
        self.d = d
        super().__init__(
        The number of bytes required to hold a specific long number.
        x = (x + a_i * M_i * inv) % m
    """
    """Chinese Remainder Theorem.
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb"""
    """Returns the inverse of x % n under multiplication, a.k.a x^-1 (mod n)
    #      or      j = multiplicitive inverse of b mod a
    # Iterateive Version is faster and uses much less stack space
    # Neg return values for i or j are made positive mod b or a respectively
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    (divider, inv, _) = extended_gcd(x, n)
    :param a_values: the a-values of the above equation
    :param div: Division's divisor, a number
    :param modulo_values: the m-values of the above equation
    :param num:
    :param num: Division's numerator, a number
    :param number:
    :return: Rounded up result of the division between the parameters.
    :returns:
    :returns: x such that x = a[i] (mod m[i]) for each i
    >>> (inverse(143, 4) * 143) % 4
    >>> crt([2, 3, 0], [7, 11, 15])
    >>> crt([2, 3, 2], [3, 5, 7])
    >>> crt([2, 3], [3, 5])
    >>> inverse(7, 4)
    0 bits.
    1
    135
    23
    3
    8
    Calculates x such that x = a[i] (mod m[i]) for each i.
    def __init__(self, *args, **kwargs): pass
    def __init__(self, a: int, b: int, d: int, msg: str = "") -> None:
    doctest.testmod()
    except AttributeError as ex:
    for m_i, a_i in zip(modulo_values, a_values):
    for modulo in modulo_values:
    if divider != 1:
    if lx < 0:
    if ly < 0:
    if mod:
    if number == 0:
    import doctest
    lx = 1
    ly = 0
    m = 1
    Number of bits needed to represent a integer excluding any prefix
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    quanta, mod = divmod(num, div)
    return a, lx, ly  # Return only positive values
    return ceil_div(bit_size(number), 8)
    return inv
    return quanta
    return x
    Returns the ceiling function of a division between `num` and `div`.
    Returns the number of bytes required to hold a specific long number.
    The number of bytes is rounded up.
    try:
    Usage::
    while b != 0:
    x = 0
    y = 1
"""Common functionality shared by several modules."""
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
class NotRelativePrimeError:
def bit_size(num: int) -> int:
def byte_size(number: int) -> int:
def ceil_div(num: int, div: int) -> int:
def crt(a_values: typing.Iterable[int], modulo_values: typing.Iterable[int]) -> int:
def extended_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
def inverse(x: int, n: int) -> int:
if __name__ == "__main__":
import typing
