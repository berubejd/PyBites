#!/usr/bin/env python3.8

import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    word_list = []

    with open(DICTIONARY) as word_file:
        word_list = [line.strip() for line in word_file.readlines()]

    return word_list

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0

    try:
        for letter in word:
            score += LETTER_SCORES[letter.upper()]

        return score
    except:
        return 0

def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    return max(words, key=calc_word_value)


print(load_words()[:10])
print(calc_word_value('bob'))