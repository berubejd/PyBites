#!/usr/bin/env python3.8

import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

from collections import defaultdict

def create_chart():
    with open(SAFARI_LOGS) as logs:
        safari = defaultdict(str)
        last_line = None

        for log in logs:
            log = log.strip()

            if log.endswith('slack channel'):
                date = log.split()[0]

                if "python" in last_line.lower():
                    safari[date] += PY_BOOK
                else:
                    safari[date] += OTHER_BOOK

            last_line = log

        for k, v in safari.items():
            print(f"{k} {v}")


create_chart()

'''
Bite 48. Make a bar chart of new Safari books ☆
Some time ago we made a little Slack bot to post new titles added to Safari to Slack. And luckily we added logging so we have some data for you to play with :)

In this Bite you will make a small bar chart of the amount of books it sent every day in February. To limit the data we just look at 10 days worth of data.

The log is loaded into the template code and has this format:

02-13 01:59 root         DEBUG    9781788838542 - WinOps - DevOps on the Microsoft Azure Stack: VSTS and TFS 2018
02-13 01:59 root         DEBUG    - sending to slack channel
02-13 01:59 root         DEBUG    9781787285217 - Python Web Scraping Cookbook
02-13 01:59 root         DEBUG    - cached, skipping
...
02-13 04:59 root         DEBUG    9781788838115 - JIRA Administration - Getting Started with JIRA
02-13 04:59 root         DEBUG    - cached, skipping
02-13 05:59 root         DEBUG    9780134858968 - My Windows 10 (includes video and Content Update Program)
02-13 05:59 root         DEBUG    - sending to slack channel
02-13 05:59 root         DEBUG    9781788838542 - WinOps - DevOps on the Microsoft Azure Stack: VSTS and TFS 2018
02-13 05:59 root         DEBUG    - cached, skipping
...
You need to count the sending to slack channel entries and look at the book title in the previous line (yes we like to challenge you!) - and see if it was a Python book. If so print 🐍 , else a dot (constants provided).

Here is the output you need to achieve. No need to return, just print it, our pytest code just calls your function and checks the stdout it returns.

02-13 ...........
02-14 ..............
02-15 .................
02-16 ............
02-19 🐍.......🐍
02-20 ...
02-21 ..............🐍
02-22 🐍...................
'''