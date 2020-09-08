#!/usr/bin/env python3.8


def round_even(number):
    """Takes a number and returns it rounded even"""
    return round(number)


for i in [
    0.4,  # 0
    0.5,  # 0
    0.6,  # 1
    1.4,  # 1
    1.5,  # 2
    2.5,  # 2
]:
    print(round_even(i))
