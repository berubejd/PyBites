#!/usr/bin/env python3.8
"""
Bite 289. Round to next number ☆
Write a function that accepts a number and a multiple, then rounds the number towards the next multiple.
"""
from math import ceil


def round_to_next(number: int, multiple: int):
    return ceil(number / multiple) * multiple