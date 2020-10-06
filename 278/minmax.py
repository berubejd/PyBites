#!/usr/bin/env python3.8
"""
Bite 278. Major and minor numbers ☆
You are given a list of integers. Write code to find the majority and minorty numbers in that list.

Definition: a majority number is the one appearing most frequently, a minority number appears least frequently.

Here is a simple example how it should work:

>>> numbers = [1, 2, 2, 3, 2, 3]
>>> major_n_minor(numbers)
(2, 1)
"""

from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    c = Counter(numbers)
    major = c.most_common()[0][0]
    minor = c.most_common()[-1][0]

    # major = max(c, key=c.get)
    # minor = min(c, key=c.get)

    return major, minor


print(major_n_minor([1, 2, 2, 3, 2, 3]))