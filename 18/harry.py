#!/usr/bin/env python3.8

import os
import urllib.request

import re
import string
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(harry_text) as fp:
        text = fp.read().lower().split()

    with open(stopwords_file) as fp:
        stopwords = fp.read().split()

    sanitized = []

    for word in text:
        new_word = ''

        for c in word:
            if c in string.ascii_letters:
                new_word = new_word + c

        if len(new_word):
            sanitized.append(new_word)

    return Counter([word for word in sanitized if word not in stopwords]).most_common()[0]

print(get_harry_most_common_word())
