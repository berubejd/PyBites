#!/usr/bin/env python3.8

from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

from pprint import pprint as pp

# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    page = BeautifulSoup(content, features="html.parser")
    table = page.find("table", {"class": "list-table"})
    
    for row in table.findAll("tr", {"class": ["holiday", "regional", "publicholiday"]}):
        month = row.find("time")["datetime"].split("-")[1]
        name = row.find("a").text.strip()
        
        holidays[month].append(name)

    return holidays


pp(get_us_bank_holidays())


'''
  >>> pp(get_us_bank_holidays())
  defaultdict(,
              {'01': ["New Year's Day", 'Martin Luther King Jr. Day'],
               '02': ["Presidents' Day"],
               '04': ['Emancipation Day'],
               '05': ["Mother's Day", 'Memorial Day'],
               '06': ["Father's Day"],
               '07': ['Independence Day'],
               '09': ['Labor Day'],
               '10': ['Columbus Day'],
               '11': ['Veterans Day', 'Thanksgiving', 'Day after Thanksgiving'],
               '12': ['Christmas Day']})
'''