#!/usr/bin/env python3.8

VOWELS = "aeiou"
PYTHON = "python"


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(map(lambda x: x in VOWELS, input_str.lower()))


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(map(lambda x: x in PYTHON, input_str.lower()))


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(map(str.isdigit, input_str))


print(contains_only_vowels("EoUia"))  # True
print(contains_only_vowels("abcde"))  # False

print(contains_any_py_chars("julian"))  # True
print(contains_any_py_chars("B@b"))  # True

print(contains_digits("hello2"))  # True
print(contains_digits("hello"))  # False

