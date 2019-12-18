#!/usr/bin/env python3.8

from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    with requests.Session() as session:
        response = session.get(PACKT)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)
            return None

    soup = Soup(response.text, "lxml")

    # Extract title
    title = soup.find("div", class_="dotd-title").text.strip()

    # Extract description
    description_div = soup.find("div", class_="dotd-main-book-summary")
    description = description_div.find_all("div")[2].text.strip()

    # Extract image and link
    image_div = soup.find("div", class_="dotd-main-book-image")
    image = image_div.img["src"]
    link = image_div.a["href"]

    return Book(title, description, image, link)


print(get_book())

"""
Bite 49. Scrape Packt's html with BeautifulSoup ☆
In this Bite you will parse Packt's free learning ebook site extracting the html for the daily free ebook:
Packt's free learning resource

As this page is changing all the time (and to not hit their servers too much) we saved a copy of the html on our server and loaded it into CONTENT

Now the best part: meet your new best friend when dealing with HTML: BeautifulSoup, a module that makes dealing with html a breeze.

Get coding: complete get_book by making a Soup object and parsing out the relevant fields as defined in Book. Next populate and return this namedtuple.

Have fun and keep calm and code in Python!
"""
