#!/usr/bin/env python3.8

num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds

    total = sum(numbers)
    num_hundreds += total // 100

    return total


lists = [
    [],  # 0, -1
    [1, 2, 3],  # 6, -1
    [40, 50, 60],  # 150, 0
    [140, 50, 60],  # 250, 2
    [140, 150, 160],  # 450, 6
    [1140, 150, 160],  # 1450, 20
]

for l in lists:
    print(sum_numbers(l), num_hundreds)

"""
Bite 254. Global vs local variables ☆
This Bite is to illustrate scoping. You will sum numbers while keeping track of number of hundreds in a global variable called num_hundreds.

To illustrate this see this REPL output:

>>> from scoping import sum_numbers, num_hundreds
>>> num_hundreds
-1
>>> sum_numbers([10, 20, 70])
100
>>> from scoping import num_hundreds
>>> num_hundreds
0
>>> sum_numbers([10, 120, 180])
310
>>> from scoping import num_hundreds
>>> num_hundreds
3

We planned to also illustrate nonlocal, but we will do that in a separate Bite ... Good luck and keep calm and code in Python!
"""
