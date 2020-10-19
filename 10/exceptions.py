#!/usr/bin/env python3.8
"""
Bite 10. Practice exceptions ☆
In this bite you learn to catch/raise exceptions.

Write a simple division function meeting the following requirements:

when denominator is 0 catch the corresponding exception and return 0.
when numerator or denominator are not of the right type reraise the corresponding exception.
if the result of the division (after surviving the exceptions) is negative, raise a ValueError
As always see the tests written in pytest to see what your code need to pass. Have fun!
"""


def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError

    if result < 0:
        raise ValueError

    return result


print(positive_divide(-2, 1))
