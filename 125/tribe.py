#!/usr/bin/env python3.8

from collections import Counter

from bs4 import BeautifulSoup
import requests

from pprint import pprint as pp

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode("utf-8")


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()

    book_list = []

    soup = BeautifulSoup(content, "html.parser")

    for link in soup.find_all("a", href=lambda href: href and AMAZON in href):
        book_list.append(link.text)

    return [book for book in Counter(book_list).most_common() if book[1] >= MIN_COUNT]


if __name__ == "__main__":
    top_5 = get_top_books()
    pp(top_5)

"""
Bite 125. Get the most recommended books ☆
The Tim Ferriss Show is full of wisdom and inspiration. It can also fill up your book shelves because a lot of awesome titles get recommended.

This raises the question: which books to prioritise? We found this list but for some the Top Books (2 or more mentions) might still be daunting!

Luckily we are PyBites Ninjas so what if we use some BeautifulSoup to scrape this site (we'll use a static copy) for the books that are at the top of this Top Books list.

Complete get_top_books below to find the number (limit) of books we could prioritise. Not surprisingly Sapiens is one of them :)
"""
