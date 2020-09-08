#!/usr/bin/env python3.8


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    return sorted(words, key=lambda x: "zzzz" + str(x) if x[0].isdigit() else x.lower())


words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
print(sort_words_case_insensitively(words))
