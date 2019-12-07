#!/usr/bin/env python3.8

from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_

def test_fizzbuzz():

    # Test non-matching case
    assert fizzbuzz(-1) == -1
    assert fizzbuzz(1) == 1
    assert fizzbuzz(11) == 11

    # Test 'Fizz' cases
    assert fizzbuzz(-3) == 'Fizz'
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(12) == 'Fizz'

    # Testing Buzz cases
    assert fizzbuzz(-5) == 'Buzz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'

    # Test 'Fizz Buzz' cases
    assert fizzbuzz(-15) == 'Fizz Buzz'
    assert fizzbuzz(0) == 'Fizz Buzz'
    assert fizzbuzz(15) == 'Fizz Buzz'
