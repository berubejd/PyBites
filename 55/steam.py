#!/usr/bin/env python3.8

from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple("Game", "title link")


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""

    return [Game(entry.title, entry.link) for entry in feedparser.parse(FEED_URL).entries]

print(get_games())