#!/usr/bin/env python3.8


def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in range(100, 0, -1):
        yield i


from itertools import islice

cd = countdown()
results = list(islice(cd, 0, 100))
print(results)

next(cd)
