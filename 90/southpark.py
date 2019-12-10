#!/usr/bin/env python3.8

from collections import Counter, defaultdict
import csv

import requests

from typing import DefaultDict

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content: str) -> DefaultDict:
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    scratch = defaultdict(defaultdict)
    words = defaultdict(Counter)
    
    reader = csv.DictReader(content.splitlines())

    for line in reader:
        character = line['Character']
        episode = line['Episode']
        count = len(line['Line'].split())
        scratch[character][episode] = scratch[character].get(episode, 0) + count
        
    for k, v in scratch.items():
        words[k] = Counter(v)

    return words


content = get_season_csv_file(1)
print(get_num_words_spoken_by_character_per_episode(content)['Cartman'])



'''
Did we already tell you we love the collections module? In this Bite we combine its defaultdict
and Counter data structures for powerful data querying.

We will use this cool South Park data set (thanks Peter for the idea and collaboration on this one!).
See the template below: we already completed get_season_csv_file to load in the csv data for a given season.

You need to complete get_num_words_spoken_by_character_per_episode which receives the loaded csv
data (example) and parse it into a defaultdict of Counter objects (don't forget to split by newlines
first). Here is a snippet what you should end up with:

              {'Agent 1': Counter({'8': 48, '2': 1}),
...
# Counter k,v here = (episode, # number of words spoken)
...
               'Anthropologist': Counter({'12': 101}),
...
               'Cartman': Counter({'1': 735,
                                   '10': 669,
                                   '13': 621,
... etc ...

Why is this cool? This structure makes it easy to do lookups by character, for example: Cartman was
most talkative in episode 1, Agent 1 in episode 8, etc. See more checks under the TESTS tab. Ready
to add collections to your toolkit? Have fun!
'''
