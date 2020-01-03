#!/usr/bin/env python3.8

def fizzbuzz(num):
    tada = []

    if num % 3 == 0:
        tada.append("Fizz")

    if num % 5 == 0:
        tada.append("Buzz")

    return ' '.join(tada) if tada else num


for num in range(1,16):
    print(f"{num} - {fizzbuzz(num)}")

"""
Bite 46. You are a programmer! Code Fizz Buzz ☆
Here is a beginner Bite to write Fizz Buzz:

Fizz buzz is a group word game for children to teach them about division. Players 
take turns to count incrementally, replacing any number divisible by three with 
the word "fizz", and any number divisible by five with the word "buzz".
...
For example, a typical round of fizz buzz would start as follows:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ..

Complete the fizzbuzz function below, it should take a number and return the right 
str or int.

If you want to write this TDD-style, consider doing Code Challenge 45 instead.

See also Coding Horror's Why Can't Programmers.. Program? for a fun read.
"""