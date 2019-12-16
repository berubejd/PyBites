#!/usr/bin/env python3.8

from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year: int) -> str:
    """Given year 'year' return the automaker that released
       the highest number of new car models"""

    return Counter([car['automaker'] for car in data if car['year'] == year]).most_common()[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""

    return set([car['model'] for car in data if car['automaker'] == automaker and car['year'] == year])

print(most_prolific_automaker(2013))
print(get_models('Mercedes-Benz', 2007))



'''
Bite 130. Analyze some basic Car Data ☆
In this exercise you will analyze some basic car data. Here is the (fake) JSON data we created with Mockeroo - snippet below / full output here:

  [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
   {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
   {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
   ... 997 car entries more ...
  ]
First you will write most_prolific_automaker to find out which automaker produces the most new models for a particular year.

Secondly you will write get_models which filters the data set down to car models produced by a particular automaker and year (as passed into the function).

To keep it a Beginner Bite we'll pause here, but if you like this data set, let us know and we make a follow-up Bite, maybe we can add some financial data :)

Check out the docstrings and pytests and give it a shot. Good luck and keep calm keep and code in Python.
'''
