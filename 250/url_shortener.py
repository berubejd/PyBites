#!/usr/bin/env python3.8

from math import floor
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"

from pprint import pprint as pp


def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    remainder = record % BASE

    result = CODEX[remainder]

    queue = floor(record / BASE)

    while queue:
        remainder = queue % BASE
        queue = floor(queue / BASE)
        result = CODEX[remainder] + result

    return result


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    value = 0

    for char in short_url:
        value = BASE * value + CODEX.find(char)

    return value


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    if not url.startswith(SITE):
        return INVALID

    link_ptr = decode(url.split("/")[-1])

    return LINKS.get(int(link_ptr), NO_RECORD)


def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    link_ptr = encode(next_record)
    LINKS[int(next_record)] = url

    return f"{SITE}/{link_ptr}"


print(encode(5120))
print(decode("1kA"))
print(redirect("https://pybit.es/J"))
print(shorten_url("https://python.org", 7000))  # https://pybit.es/1OU
print(redirect("https://pybit.es/1OU"))
pp(LINKS)


"""
Bite 250. PyBites URL Shortener ☆
URL shortening is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may 
be made substantially shorter and still direct to the required page (Wikipedia). Let's build one 
for PyBites!

You would think that there is some complex math involved here, but that's not really what's going 
on. The only thing that's encoded is the database record ID of the URL entry.

Since we're only interested in encoding 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 
we will be encoding the values into Base62. Why 62? Well because if you add up all of those characters, 
they total 62! If you wanted to use other symbols, that would be a great exercise for you to expand on 
what you learn here.

If you don't know how to encode numbers into other base formats, here's a quick little tutorial:

# encode(100):
num = 100
# num % base62
remainder = 100 % 62 = 38
# codex[remainder]
result = codex[38]  # "C"

# floor(num / base62)
queue = floor(100 / 62)  # 1

while queue:
    # queue % base62
    remainder = 1 % 62  # 1
    # floor(queue / base62)
    queue = floor(1 / 62)  # 0
    # codex[remainder] + result
    result = codex[1] + "C"  # "1C"
return result

# decode("1C")
value = 0
for char in result:
    # first pass char = 1
        # value = base62 * value + codex.find(char)
        # value = 62 * 0 + codex.find("1")
        # value = 0 + 1
    value = 1
    # second pass char = C
        # value = base62 * value + codex.find(char)
        # value = 62 * 1 + codex.find("C")
        # value = 62 + 38
    value = 100
return value

Instead of using an SQL database or something like that, for this Bite we'll just be using the LINKS 
dictionary. I've provided some code to get you started, but you'll have to complete the following functions:

encode: Encodes the number passed into Base62
decode: Decodes the string passed back into Base10
redirect: Takes a shortened URL and returns the URL stored in LINKS
Verifies that domain of shortened url is from https://pybit.es, if not returns error message INVALID
Checks to see if the record exists, if not return error message NO_RECORD
Returns the stored URL
shorten_url: Shortens the URL and updates LINKS
Encodes the next_record passed to it
Adds the URL to LINKS
Returns the shortened URL
And apart from the included tests, here you can see it in action in the REPL:

>>> from url_shortener import encode, decode, redirect, shorten_url
>>> encode(5120)
'1kA'
>>> decode('1kA')
5120
>>> shorten_url("https://python.org", 7000)
'https://pybit.es/1OU'
>>> redirect('https://pybit.es/1OU')
'https://python.org'

An URL shortener is a pretty useful service to provide, so let's give it a shot. Have fun and keep calm and code in Python!
"""
