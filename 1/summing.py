#!/usr/bin/env python3.8

def sum_numbers(numbers=None) -> int:
    '''
    Write a function that can sum up numbers:

     - It should receive a list of n numbers.
     - If no argument is provided, return sum of numbers 1..100.
     - Look closely to the type of the function's default argument
    '''
    if numbers == None:
        numbers = range(1,101)

    return sum(numbers)

print(sum_numbers())
print(sum_numbers(numbers=None))

print(sum_numbers(range(1, 11)))
print(sum_numbers([1,2,3]))
print(sum_numbers([]))