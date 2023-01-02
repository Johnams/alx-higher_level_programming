#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """Returns an integer: the addition of a and b.
    a and b to be casted to integers if they are floats

    Raise:
        TypeError: If either of a or b is non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b is not an integer")
    return (int(a) + int(b))
