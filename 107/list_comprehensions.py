#!/usr/bin/env python3.8

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""

    return [number for number in numbers if number > 0 and number % 2 == 0]

num_list = list(range(-10, 11))

print (filter_positive_even_numbers(num_list))
