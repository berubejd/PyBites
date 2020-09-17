#!/usr/bin/env python3.8
"""
In this Bite you complete find_number_pairs which receives a list of 
numbers and returns all the pairs that sum up to N (default=10). Return 
this list of tuples from the function.

So in the most basic example if we pass in [2, 3, 5, 4, 6] it 
returns [(4, 6)] and if we give it [9, 1, 3, 8, 7] it returns 
[(9, 1), (3, 7)]. The tests check more scenarios (floats, other values 
of N, negative numbers).
"""

from itertools import combinations


def find_number_pairs(numbers: list, N: int = 10) -> list:
    # results = []
    # for test in combinations(numbers, 2):
    #     if test[0] + test[1] == N:
    #         results.append(test)
    # return results

    return [test for test in combinations(numbers, 2) if test[0] + test[1] == N]


print(find_number_pairs([0.2, 9.8, 10, 1, 0], 10))
