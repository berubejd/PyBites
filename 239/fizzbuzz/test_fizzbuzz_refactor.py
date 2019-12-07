#!/usr/bin/env python3.8

import pytest
from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize("arg, ret", [
    (-5, "Buzz"),
    (-4, -4),
    (-3, "Fizz"),
    (-2, -2),
    (-1, -1),
    (0, "Fizz Buzz"),
    (1, 1),
    (2, 2),
    (3, "Fizz"),
    (4, 4),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, 7),
    (8, 8),
    (9, "Fizz"),
    (10, "Buzz"),
    (11, 11),
    (12, "Fizz"),
    (13, 13),
    (14, 14),
    (15, "Fizz Buzz"),
])
def test_fizzbuzz(arg, ret):
    # Test all cases using arg and ret from parameterize
    assert fizzbuzz(arg) == ret

