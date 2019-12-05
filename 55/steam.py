#!/usr/bin/env python3.8

from collections import namedtuple

from bs4 import BeautifulSoup
import feedparser

from pprint import pp

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple("Game", "title link")


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    
    game_list = []
    
    rss_data = feedparser.parse(FEED_URL)
    
    for entry in rss_data.entries:
        soup = BeautifulSoup(entry.summary, "html.parser")
        link = soup.find("a")
        game_list.append(Game(link.text, link["href"]))

    return game_list

print(get_games())