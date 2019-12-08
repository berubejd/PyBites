#!/usr/bin/env python3.8

import pytest

from numbers_to_dec import list_to_decimal

def test_list_to_decimal():
    # Test TypeError for input other than int
    with pytest.raises(TypeError):
        list_to_decimal(['Test'])

    with pytest.raises(TypeError):
        list_to_decimal([None])

    with pytest.raises(TypeError):
        list_to_decimal([True])

    # Test ValueError for int input out of range
    with pytest.raises(ValueError):
        list_to_decimal([-1])

    with pytest.raises(ValueError):
        list_to_decimal([10])

    with pytest.raises(ValueError):
        list_to_decimal([1000])

    # Test correct output for inputs of correct type
    assert list_to_decimal([1]) == 1
    assert list_to_decimal([0,1]) == 1
    assert list_to_decimal([1,0]) == 10
    assert list_to_decimal([1,1]) == 11