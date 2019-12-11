#!/usr/bin/env python3.8

import csv
import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'

from collections import defaultdict


def get_csv() -> dict:
    """Use requests to download the csv and return the
       decoded content"""
    r = requests.get(CSV_URL)

    reader = csv.DictReader(r.text.splitlines())

    return (row for row in reader)


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    users = defaultdict(int)

    for row in content:
        users[row["tz"]] += 1

    for key in sorted(users.keys()):
        bar = "+" * users[key]

        print(f"{key:<21}| {bar}")

create_user_bar_chart(get_csv())

'''
Bite 79. Parse a csv file and create a bar chart ☆
We played a bit with the Slack API today and wow: our PyBites community is super international! We really enjoy connecting with Pythonistas from all over the globe.

We put some anonymized data in a csv (using uuid4 and faker) and for this Bite we ask you to use requests to load it in, use the csv module to parse it into a data structure of your choice, and finally produce the following output:

Africa/Algiers       | ++
Africa/Cairo         | +
Africa/Monrovia      | +
Africa/Nairobi       | ++++
...
...
Europe/Moscow        | ++
Europe/Warsaw        | ++
Pacific/Honolulu     | +
See the full output under the TESTS tab. Good luck and remember: keep calm and code in Python!
'''