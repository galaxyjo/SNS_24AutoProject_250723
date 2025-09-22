# 📄 modules/common/random_custom.py (리팩토링 후 전체 복붙용)
"""Wrapper module for Python's random utilities with simplified interface."""

import random
from typing import Sequence, Any


def randint(a: int, b: int) -> int:
    """Return random integer N such that a <= N <= b."""
    return random.randint(a, b)


def randrange(*args: int) -> int:
    """
    Return a randomly selected element from range(*args).

    Supports:
    - randrange(stop)
    - randrange(start, stop)
    - randrange(start, stop, step)
    """
    if len(args) == 1:
        return random.randrange(args[0])
    elif len(args) == 2:
        return random.randrange(args[0], args[1])
    elif len(args) == 3:
        return random.randrange(args[0], args[1], args[2])
    else:
        raise ValueError(
            "randrange expected at most 3 arguments, got %d" % (len(args),)
        )


def choice(seq: Sequence[Any]) -> Any:
    """Return a random element from the non-empty sequence."""
    return random.choice(seq)


def sample(population: Sequence[Any], k: int) -> list[Any]:
    """Return a k-length list of unique elements chosen from the population."""
    return random.sample(population, k)


def shuffle(x: list[Any]) -> None:
    """Shuffle the sequence in place."""
    random.shuffle(x)


def getrandbits(k: int) -> int:
    """Return an int with k random bits."""
    return random.getrandbits(k)
