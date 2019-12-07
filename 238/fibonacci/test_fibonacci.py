#!/usr/bin/env python3.8

from fibonacci import fib

import pytest

# write one or more pytest functions below, they need to start with test_

def test_fib():
    # Test n < 0
    with pytest.raises(ValueError):
        fib(-1)

    # Test inputs of either 0 or 1 return input
    assert fib(0) == 0
    assert fib(1) == 1

    # Test inputs of larger numbers
    assert fib(2) == 1
    assert fib(3) == 2