#!/usr/bin/env python3.8

from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    return (
        round(acc_total / count, 2)
        for count, acc_total in enumerate(accumulate(sequence), 1)
    )


ret = list(running_mean([2, 6, 10, 8, 11, 10])) # [2.0, 4.0, 6.0, 6.5, 7.4, 7.83]
print(ret)


"""
Bite 66. Calculate the running average of a sequence ☆
Write a function that takes a sequence of items and returns the running average, so for example this:

running_mean([1, 2, 3])
returns:
[1, 1.5, 2]
You can assume all items are numeric so no type casting is needed.

Round the mean values to 2 decimals (4.33333 -> 4.33). See the tests for more info.

Bonus: use a function of itertools + make it a generator, but this is not required to get this working.
"""
