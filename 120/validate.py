#!/usr/bin/env python3.8

from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*args, **kwargs):

        for arg in args:
            if not type(arg) == int:
                raise TypeError

            if arg < 0:
                raise ValueError

        return func(*args, **kwargs)

    return wrapped


"""
Bite 120. Write a numbers validation decorator ☆
Let's get some more practice with decorators ... in this Bite you will write a decorator 
that checks if input arguments (*args *1) are positive integers. If one or more of the 
passed in args are not of type int, it throws a TypeError, if it is an int but < 0, it 
throws a ValueError.

That's it! Wrap it in a nice decorator and the tests will validate your code. Have fun!
"""
