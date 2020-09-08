#!/usr/bin/env python3.8


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return len(text) - len(text.lstrip(" "))


print(count_indents("string "))  # 0
print(count_indents("  string"))  # 2
print(count_indents("    string"))  # 4
print(count_indents("\t\tstring"))  # 0
