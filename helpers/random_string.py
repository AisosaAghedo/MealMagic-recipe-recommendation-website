#!/usr/bin/python3
import random
import string


def string_gen(length):
    """
    returns a random string using the length arg to determine
    how many characters
    """
    chars = string.ascii_letters + string.digits

    # Generate the random string
    random_string = ''.join(random.choice(chars) for _ in range(length))
    return random_string
