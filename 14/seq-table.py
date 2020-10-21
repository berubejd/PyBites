#!/usr/bin/env python3.8
"""
Bite 14. Generate a table of n sequences ☆
Write a function that receives one or more sequences. The sequences are already defined for you.

The function should return a table (list of strings) where the columns are the sequences (example below).

To keep it simple we work with equally sized sequences so you don't have to worry about handling a missing value (you should end up with a grid of 6 rows x n columns).

There are some Pythonic idioms you can use here, hint: think of pants ;)

Example call (look at the tests for more detail):

>>> generate_table(names, aliases)
['Julian | Pythonista', 'Bob | Nerd', 'PyBites | Coder', 
 'Dante | Pythonista', 'Martin | Nerd', 'Rodolfo | Coder']
Bonus: use a generator to build up the table rows.
"""
import random

names = "Julian Bob PyBites Dante Martin Rodolfo".split()
aliases = "Pythonista Nerd Coder".split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "


def generate_table(*args):
    for row in zip(*args):
        yield SEPARATOR.join(str(column) for column in row)


print(list(generate_table(names, aliases, points)))