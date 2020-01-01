#!/usr/bin/env python3.8

from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = "https://bites-data.s3.us-east-2.amazonaws.com/" "best-programming-books.html"
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """

    def __init__(self, title: str, author: str, year: int, rank: int, rating: float):
        self.title = title
        self.author = author
        self.year = int(year)
        self.rank = int(rank)
        self.rating = float(rating)

    def __str__(self):
        book_str = (
            f"[{self.rank:03}] {self.title} ({self.year})\n"
            f"      {self.author} {self.rating}"
        )

        return book_str


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    if not year:
        year = 0

    return [
        print(book)
        for book in list(filter(lambda x: x.year >= int(year), books))[:limit]
    ]


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    book_list = []

    soup = _get_soup(html_file)

    books = soup.select(".book")

    for book in books:
        # Grabbing the book class includes the title as an attribute but they want this one
        title = book.select_one(".book-title .main").text

        if "python" in title.lower():
            # Capture the *first* author on multi-author books
            author = book.select_one(".authors").text.split(",")[0].split()
            author = f"{author[-2]}, {' '.join(author[:-2])}"

            # Capture the year and continue if it doesn't exist
            try:
                year = book.select_one(".date").text.split()[1]
            except:
                continue

            # Capture the rating
            rating = book.select_one(".our-rating").text

            # Create the book object now that we have all the data
            # -> I am not going to pull the publication rank as it will be immediately overwritten
            book_list.append(
                Book(title=title, author=author, year=year, rank=0, rating=rating)
            )

    # Sort books: descending by rating and ascending by year, title, and then by author's last name
    book_list.sort(key=lambda x: (x.year, x.title.lower(), x.author.lower()))
    book_list.sort(key=lambda x: x.rating, reverse=True)

    # Set book rankings
    for rank, book in enumerate(book_list, 1):
        book.rank = rank

    return book_list


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""


"""
Bite 229. Scrape best programming books ☆
For this bite, you are going to scrape the books from 100 Best Programming Books of All Time. Only include the ones with the word python in their titles (case insensitive match).

Since the page gets generated via JavaScript, we will be providing you with the source and the code to load it up and bundle it into a BeautifulSoup object for you. All you will have to do is scrape the necessary data and create Book objects from it.

The Book class
Create a class for the books which should have the following class variables:

title: string as it appears on the page
author: string should be entered as lastname, firstname
year: four digit integer year that the book was published
rank: integer rank to be updated once the books have been sorted
rating: float as indicated on the page
When you print a Book it should be formatted as follows:

[001] Python Tricks (2017)
      Bader, Dan 4.74
The load_data() function
With this function you will load the data from the html_file. This is where you will call the _get_soup() function that has been provided for you.

Loads the soup object
Extract the information from the soup object required to create the Book instances
Returns a sorted list of Book objects
NOTE: If any of the required attributes is missing from any of the books, dump the book and don't include it.

SORTING: Books should be sorted descending by rating and ascending by year, title, and then by author's last name; in that order. When sorting the titles, make sure to sort them with either .title(), .lower(), or .upper() but take care not to change the original.

RANKING: After the books have been sorted, the rank of each book needs to be updated to indicate this new sorting order.The Book object with the highest rating should be first and go down from there.

The display_books() function
With this function, you are simply going to print the specified books to the console. You will need to implement the following variables:

books: list of all the sorted Books
limit: integer that indicates how many books to return, defaults to 10
year: integer indicating the oldest year to include, i.e. 2017, defaults to None
If it's called with more books than are in the list, it should only display the max books that are available and not fail.

Sample call to display_books():
display_books(books, limit=5, year=2017)

[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
NOTE: Notice that the books ranking 003, 004, and 005 are not listed. That's because I specified that the oldest date to include as 2017 and those books were older then that. Another point to note, is that books ranking 006 and 007 both have the same rating, book titles, and release dates but they were sorted by the author's last name!

This is an advanced bite, so don't despair! Keep at it and you will emerge victorious! I look forward to seeing your submissions in the forum!
"""
