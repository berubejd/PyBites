#!/usr/bin/env python3.8

import string

ALPHANUM = string.ascii_letters + string.digits

def get_index_different_char(chars) -> int:
    alpha = []
    non_an = []

    for pos, char in enumerate(chars):
        if char:
            if str(char) in ALPHANUM:
                alpha.append((char, pos))

            else:
                non_an.append((char, pos))

    return alpha[0][1] if len(alpha) < len(non_an) else non_an[0][1]

print(get_index_different_char(['A', 'f', '.', 'Q', 2])) # 2
print(get_index_different_char(['.', '{', ' ^', '%', 'a'])) # 4
print(get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'])) # 5

"""
Bite 29. Martin's IQ test ☆
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
See the TESTS tab for more details
"""