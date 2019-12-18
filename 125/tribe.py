#!/usr/bin/env python3.8

from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = "https://bites-data.s3.us-east-2.amazonaws.com/" "tribe-mentors-books.html"


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode("utf-8")


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()

    book_list = []

    soup = BeautifulSoup(content, "html.parser")

    for link in soup.find_all("a", href=lambda href: href and AMAZON in href):
        book_list.append((link["href"], link.text))

    return [k[1] for k, v in Counter(book_list).most_common(limit)]


if __name__ == "__main__":
    top_5 = get_top_books()
    # top_10 = get_top_books(limit=10)

    print(f"Top  5: {top_5}")
    # print(f"Top 10: {top_10}")

"""
Bite 125. Get the most recommended books ☆
The Tim Ferriss Show is full of wisdom and inspiration. It can also fill up your book shelves because a lot of awesome titles get recommended.

This raises the question: which books to prioritise? We found this list but for some the Top Books (2 or more mentions) might still be daunting!

Luckily we are PyBites Ninjas so what if we use some BeautifulSoup to scrape this site (we'll use a static copy) for the books that are at the top of this Top Books list.

Complete get_top_books below to find the number (limit) of books we could prioritise. Not surprisingly Sapiens is one of them :)
"""
