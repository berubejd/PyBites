#!/usr/bin/env python3.8


def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) as file:
        contents = file.read().splitlines()
        return contents[-n:]


print(tail("file.txt", 2))
