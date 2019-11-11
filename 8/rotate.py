#!/usr/bin/env python3.8

def rotate(string: str, n: int) -> str :
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    from collections import deque

    new_string = deque(string)
    new_string.rotate(-n)

    return ''.join(new_string)

print(rotate('hello', 2)) # llohe
print(rotate('hello', -2)) # lohel
print(rotate('hello', 14))