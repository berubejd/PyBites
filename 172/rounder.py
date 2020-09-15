#!/usr/bin/env python3.8


from functools import partial
import functools


def rounder(value: float, places: int):
    return round(value, places)


# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
rounder_int = partial(rounder, places=None)
rounder_detailed = partial(rounder, places=4)


print(rounder_int(1.3434587383))
print(rounder_detailed(1.344587383))
