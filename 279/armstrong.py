#!/usr/bin/env python3.8
"""
Bite 279. Armstrong numbers ☆
In number theory there are many interesting numbers - eg. Armstrong numbers, Happy numbers, Meertens numbers, just name a few.

In this bite, you will try to solve the Armstrong number question: given an integer, determine if it is an armstrong number.

An armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. See this reference for more info and here are some examples:

a) 153 is an armstrong number. It's a 3 digits number:

    (1^3) + (5^3) + (3^3)= 153.

b) 371 is also an armstrong number.
c) any single digit numbers (1-9) are armstrong numbers as well.
"""


def is_armstrong(n: int) -> bool:
    power = len(str(n))
    total = 0

    for p in str(n):
        total += int(p) ** power

    return total == n


print(is_armstrong(152))  # False
print(is_armstrong(153))  # True
