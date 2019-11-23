#!/usr/bin/env python3.8

import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

### Starting here

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""

    return [perm.lower() for perm in _get_permutations_draw(draw) if perm.lower() in dictionary]

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    
    for length in range(1, len(draw) + 1):
        for perm in itertools.permutations(draw, length):
            yield ''.join(perm)


draw = 'G, A, R, Y, T, E, V'
draw = draw.split(', ')

words = get_possible_dict_words(draw)
print(max_word_value(words))