#!/usr/bin/env python3.8

import math

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33]


def round_up_or_down(transactions: list, up: bool = True) -> list:
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    # func = math.ceil if up else math.floor
    # return [func(t) for t in transactions]

    if up:
        return [math.ceil(transaction) for transaction in transactions]
    else:
        return [math.floor(transaction) for transaction in transactions]


print(round_up_or_down(transactions1, True))  # [3, 4, 5, 11, 101]
print(round_up_or_down(transactions2, False))  # [1, 9, 5, 6, 2]

