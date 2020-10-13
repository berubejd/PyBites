#!/usr/bin/env python3.8
"""
Bite 293. N digit numbers ☆
Write a function that accepts a list of numbers and converts them into n digit integers.

Examples:  

n_digit_numbers([1, 2, 3], 2)  => [10, 20, 30]

n_digit_numbers([8, 9, 10], 2)  => [80, 90, 10]

n_digit_numbers([-1.1, 2.22, -3.333], 3)  => [-110, 220, -333]
Note: Negative numbers should keep their negativity and calling the function with n < 1 should raise a ValueError.
"""
from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError

    return [
        int(str(digit * (10 ** (n)))[: n if digit > 0 else n + 1]) for digit in numbers
    ]


print(n_digit_numbers([8, 9, 10], 2))  # [80, 90, 10]
print(n_digit_numbers([-1.1, 2.22, -3.333], 3))  # [-110, 220, -333]
