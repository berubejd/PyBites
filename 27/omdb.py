#!/usr/bin/env python3.8

import json

from pathlib import Path
from urllib.request import urlretrieve

TMP = Path('/tmp')
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)

files = []

with open(DATA_LOCAL) as fp:
    for i, line in enumerate(fp.readlines(), 1):
        movie_json = TMP / f'{i}.json'

        with open(movie_json, 'w') as fp:
            fp.write(f'{line}\n')

        files.append(movie_json)


import re


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_data = []

    for file in files:
        with open(file, "r") as fp:
            movie_data.append(json.loads(fp.read()))

    return movie_data


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    movie_list = []

    for movie in movies:
        if 'nominations' in movie['Awards']:
            noms = re.search(r'(\d+) nominations', movie['Awards']).group(1)
            movie_list.append({'Title': movie['Title'], 'Nominations': int(noms)})

    return max(movie_list, key=lambda x:x['Nominations'])['Title']


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    movie_list = []

    for movie in movies:
        if movie['Runtime']:
            runtime = movie['Runtime'].split()[0]
            movie_list.append({'Title': movie['Title'], 'Runtime': int(runtime)})

    return max(movie_list, key=lambda x:x['Runtime'])['Title']


movie_list = get_movie_data(files)

print(len(movie_list))
print(get_single_comedy(movie_list))
print(get_movie_most_nominations(movie_list))
print(get_movie_longest_runtime(movie_list))