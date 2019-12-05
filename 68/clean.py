#!/usr/bin/env python3.8

import string

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return input_string.translate(str.maketrans("", "", string.punctuation))

print(remove_punctuation('Hello, I am Tim.'))