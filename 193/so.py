#!/usr/bin/env python3.8

import requests
from bs4 import BeautifulSoup

cached_so_url = "https://bites-data.s3.us-east-2.amazonaws.com/so_python.html"


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    question_list = []

    with requests.Session() as session:
        response = session.get(cached_so_url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)
            return None

    soup = BeautifulSoup(response.text, "lxml")

    for container in soup.find_all("div", class_="question-summary"):
        views = container.find("div", class_="views").text.strip()

        if "m views" in views:
            question = container.find("a", class_="question-hyperlink").text
            votes = container.find("span", class_="vote-count-post").text

            question_list.append((question, int(votes)))

    return sorted(question_list, key=lambda x: x[1], reverse=True)


print(top_python_questions())

"""
Bite 193. Most upvoted StackOverflow Python questions ☆
In this Bite you parse a copy of StackOverflow Python questions which we cached here

Retrieve + parse this URL with requests + BeautifulSoup and extract the question (question-hyperlink class), votes (vote-count-post class) and number of views (views class) into a list.

Next filter the list to only show questions with more than one million views (HTML = "..m views") and sort the remaining questions descending on number of votes. See the tests for the expected return output. Some pretty good questions in that list!

Enjoy and code more Python!
"""
