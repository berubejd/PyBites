#!/usr/bin/env python3.8

from collections import namedtuple
from datetime import date

import feedparser

FEED = "https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml"

Entry = namedtuple("Entry", "date title link tags")

from pprint import pprint as pp
from datetime import datetime

from time import mktime


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date.fromtimestamp(mktime(stime))


def get_feed_entries(feed=FEED) -> list:
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    f = feedparser.parse(feed)

    entry_list = []

    for entry in f.entries:
        date = _convert_struct_time_to_dt(entry["published_parsed"])
        title = entry["title"]
        link = entry["link"]
        tags = [tag["term"].lower() for tag in entry["tags"]]

        entry_list.append(Entry(date=date, title=title, link=link, tags=tags))

    return entry_list


def filter_entries_by_tag(search, entry) -> bool:
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    tags = entry.tags
    search_words = search.strip().translate(str.maketrans("&|", "  ")).split()

    if "&" in search:
        search_type = "AND"
    else:
        search_type = "OR"

    for word in search_words:
        if word.lower() in tags:
            if search_type == "OR":
                return True

        elif search_type == "AND":
            return False

    if search_type == "OR":
        return False

    else:
        return True


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()

    while True:
        response = input("What you you like to search for? ")

        if not response:
            print("Please provide a search term")
            continue

        if response.lower() == "q":
            print("Bye")
            break

        matches = [
            entry
            for entry in list(
                filter(lambda x: filter_entries_by_tag(response.lower(), x), entries)
            )
        ]

        if matches:
            for entry in sorted(matches, key=lambda x: x.date):
                print(entry.title)

        print(f"{len(matches)} {'entry' if len(matches) == 1 else 'entries'} matched")


if __name__ == "__main__":
    main()


"""
Bite 50. Make a little PyBites search engine (feedparser) ☆
Complete the program below to create a little search command line app to search the 
PyBites blog on tags. It uses feedparser to pull in the feed (static copy to have 
the same results over time), and the search should support AND / OR searches. As 
this is an Advanced Bite not too much hand-holding, however we have added docstrings 
with some guidance. You can see an example run here.
"""
