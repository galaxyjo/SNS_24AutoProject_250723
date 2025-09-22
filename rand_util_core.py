import random


def randint(a, b):
    return random.randint(a, b)


def choice(seq):
    return random.choice(seq) if seq else None


def shuffle(seq):
    random.shuffle(seq)
    return seq


__all__ = ["randint", "choice", "shuffle"]
