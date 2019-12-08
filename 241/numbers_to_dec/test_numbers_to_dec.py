#!/usr/bin/env python3.8

import pytest

from numbers_to_dec import list_to_decimal

@pytest.mark.parametrize("arg, ret", [
                                        ([1], 1),
                                        ([0,1], 1),
                                        ([1,0], 10),
                                        ([1,1], 11)
                                    ])
def test_list_to_decimal(arg, ret):
    assert list_to_decimal(arg) == ret

def test_value_error_low():
    with pytest.raises(ValueError):
        list_to_decimal([-1])

def test_value_error_high():
    with pytest.raises(ValueError):
        list_to_decimal([10])

def test_type_error_str():
    with pytest.raises(TypeError):
        list_to_decimal(['Test'])

def test_type_error_none():
    with pytest.raises(TypeError):
        list_to_decimal([None])

def test_type_error_bool():
    with pytest.raises(TypeError):
        list_to_decimal([True])
