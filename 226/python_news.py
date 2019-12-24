#!/usr/bin/env python3.8

from collections import namedtuple

from bs4 import BeautifulSoup
import requests

from pprint import pprint as pp

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

url = "https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html"

Entry = namedtuple("Entry", "title points comments")


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    title_list = []
    points_list = []
    final_list = []

    soup = _create_soup_obj(url)

    title_entries = soup.select(".title")
    title_list = [entry.text.strip() for entry in title_entries]

    points_entries = soup.select(".controls")
    for entries in points_entries:
        # Get Points
        points = entries.select_one(".smaller").text
        points = points.split()[0]

        # Get Comments
        comments = entries.select_one(".naturaltime span a").text
        comments = comments.split()[0]

        points_tuple = (points, comments)

        points_list.append(points_tuple)

    for title, points_tuple in zip(title_list, points_list):
        entry = Entry(title, int(points_tuple[0]), int(points_tuple[1]))
        final_list.append(entry)

    return sorted(final_list, key=lambda x: x.points + x.comments, reverse=True)[:top]


pp(get_top_titles(url, 50))

"""
address = soup.find(text="Address:")
b_tag = address.parent
td_tag = b_tag.parent
next_td_tag = td_tag.findNext('td')
print next_td_tag.contents[0]
"""

"""
Bite 226. Get top titles from news.python.sc ☆
There is a new Python news aggregator in town! Check it out here. In this Bite you will parse it!

Imagine you want to email yourself and colleagues a Friday digest of top articles, based on number 
of points and comments.

Our first go would be feedparser but there is not an RSS feed yet.

So in this Bite you will use some BeautifulSoup (4.7.1) to parse the HTML yourself. Not a bad skill 
to have, no?

We have you parse a static copy of the site so we have predictable data to test your code against. 
As you can see in the tests your code should work with the second (paginated) page as well.

Note we had some issues getting lxml to work on the platform so use bs4's html.parser for now. Also 
the W3C validator does not really like the HTML so you cannot rely on article or table while parsing 
out the entries. Search for the title class instead.

Good luck and bookmark this site to keep up2date with Python news. If you see anything interesting 
feel free to share it on our Slack - #pybites-news channel.

Update 20th of Oct 2019: there is an RSS feed available now, but no count of comments/points so you 
will still need BeautifulSoup / scraping. No worries though, if you want to scrape RSS feeds, take 
one of our feedparser Bites ...

Keep calm and code more Python!



<tr id="6cce0c43-38f2-4c43-bf62-f4478d53fb95">
    <td rowspan="2" class="rank">
        31.
    </td>
    <td rowspan="2">
        <div>
        </div>
    </td>
    <td><!-- ROW 1-->  
        <div style="margin-bottom:3pt; ">            
            <span class="title">            
                <a rel="ugc" href="https://github.com/donnemartin/system-design-primer">Learn how to design large-scale systems</a>
                    <span class="smaller">(<a href="/newest?site=github.com">github.com</a>)
                    </span>
                <br />    
            </span>
        </div>
    </td>
</tr>
<tr>
    <td><!-- ROW 2--> 
        <span class="controls">
            <span class="smaller">
                3 points by
                <a class="green" href="/profile/v">v</a>
                <span class="naturaltime" data-orig-time="2019-10-11T15:12:19.405966+00:00">
                    3 days, 16 hours ago
                    <span>
                    |
                    <a href="/item/6cce0c43-38f2-4c43-bf62-f4478d53fb95">0 comments</a>
                    </span>
                </span>
            *MISSING /SPAN*
        *MISSING /SPAN*
    </td>
    </td> *DUPLICATE*
*MISSING /TR*
"""
