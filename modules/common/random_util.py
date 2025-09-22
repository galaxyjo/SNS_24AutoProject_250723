# modules/common/random_util.py

import random
import string


def random_int(min_value=0, max_value=100):
    return random.randint(min_value, max_value)


def random_float(min_value=0.0, max_value=1.0):
    return random.uniform(min_value, max_value)


def random_choice(seq):
    if not seq:
        return None
    return random.choice(seq)


def random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
