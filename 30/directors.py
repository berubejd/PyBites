#!/usr/bin/env python3.8

import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    dict_mbd = defaultdict(list)

    with open(local, newline='') as movie_metadata:
        reader = csv.DictReader(movie_metadata)
        for line in reader:
            if line['director_name'] and line['title_year'] and not int(line['title_year']) < MIN_YEAR:
                new_movie = Movie(title=line['movie_title'], year=int(line['title_year']), score=float(line['imdb_score']))
                dict_mbd[line['director_name']].append(new_movie)

    return dict_mbd   


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""

    movie_total = 0    
    movie_count = 0    

    for movie in movies:
        movie_total += movie.score
        movie_count += 1

    return round(movie_total / movie_count, 1)

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""

    # from operator import attrgetter

    Score = namedtuple('Score', 'director_name average_score')
    gas = []

    for director in directors:

        if len(directors[director]) >= MIN_MOVIES:
           # new_score = Score(director_name=director, average_score=calc_mean_score(directors[director]))
           # gas.append(new_score)
           gas.append((director, calc_mean_score(directors[director])))

    # return sorted(gas, key=attrgetter('average_score'), reverse=True)
    return sorted(gas, key = lambda x: float(x[1]), reverse=True)

director_movies = get_movies_by_director()

# print(len(director_movies['Sergio Leone']))
# print(len(director_movies['Peter Jackson']))

# movies_sergio = director_movies['Sergio Leone']
# movies_nolan = director_movies['Christopher Nolan']
# print(calc_mean_score(movies_sergio))
# print(calc_mean_score(movies_nolan))

scores = get_average_scores(director_movies)
# print(scores[0])
# print(scores[1])

# for score in scores[2:13]:
#     print(score[0])
