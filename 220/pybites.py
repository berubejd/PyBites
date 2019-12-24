#!/usr/bin/env python3.8

from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser

import functools
import os
import requests

from pathlib import Path

from pprint import pprint as pp

SPECIAL_GUEST = "Special guest"

# using _ as min/max are builtins
Duration = namedtuple("Duration", "avg max_ min_")

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = "https://bites-data.s3.us-east-2.amazonaws.com/python_bytes"
IGNORE_DOMAINS = {
    "https://pythonbytes.fm",
    "http://pythonbytes.fm",
    "https://twitter.com",
    "https://training.talkpython.fm",
    "https://talkpython.fm",
    "http://testandcode.com",
}


class PythonBytes:

    DATAFILE = Path("/tmp/pythonbytes.data")

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        if not os.path.isfile(self.DATAFILE):
            with requests.Session() as session:
                response = session.get(url)

                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    print(e)
                    return None

                with open(self.DATAFILE, "wb") as fp:
                    fp.write(response.content)

        with open(self.DATAFILE) as fp:
            feed_data = fp.read()

        self.entries = feedparser.parse(feed_data).entries

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [
            entry.itunes_episode
            for entry in self.entries
            if domain in entry.description
        ]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        domains = []
        pattern = "https?://[^/]+"

        for entry in self.entries:
            results = re.findall(pattern, entry.description)

            for domain in set(results):
                if not domain in IGNORE_DOMAINS:
                    domains.append(domain)

        return Counter(domains).most_common()[:n]

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        count = 0
        for entry in self.entries:
            if SPECIAL_GUEST in entry.description:
                count += 1

        return count

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """

        def _seconds(duration: str) -> int:
            try:
                duration = int(duration)
                return duration
            except:
                hours, mins, secs = duration.split(":")
                return int(hours) * 3600 + int(mins) * 60 + int(secs)

        durations = [entry.itunes_duration for entry in self.entries]

        avg = int(
            functools.reduce(lambda x, y: _seconds(x) + _seconds(y), durations)
            / len(durations)
        )
        max_ = max(durations, key=_seconds)
        min_ = min(durations, key=_seconds)

        return Duration(avg=avg, max_=max_, min_=min_)


REAL_PYTHON = "realpython.com"
PYBITES = "pybit.es"

pb = PythonBytes()

print(len(pb.get_episode_numbers_for_mentioned_domain(PYBITES)))  # 5
print(len(pb.get_episode_numbers_for_mentioned_domain(REAL_PYTHON)))  # 25

pp(pb.get_most_mentioned_domain_names())

print(pb.number_episodes_with_special_guest())

print(pb.get_average_duration_episode_in_seconds())


"""
Bite 220. Analysing @pythonbytes RSS feed ☆
Another feedparser exercise! In this Bite we're going to analyze the Python Bytes Podcast feed a bit completing the PythonBytes class:

Use feedparser to load the passed in feed URL into self.entries
Next complete the stubbed out methods following the docstrings: get_episode_numbers_for_mentioned_domain, get_most_mentioned_domain_names, number_episodes_with_special_guest, and get_average_duration_episode_in_seconds.
We added some type hinting and left the modules we used in the imports at the top. Also check out the tests, we use the full and partial feeds so hardcoded answers won't pass ;)

We were not sure to rate this intermediate or advanced, but this deserves 4 points for sure, so we kept it Advanced.

If you get stuck you can ask help on our Slack -> #codechallenges channel, just don't give any solutions away.

Good luck and keep calm and code in Python!
"""
