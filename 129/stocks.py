#!/usr/bin/env python3.8

import requests

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

from collections import Counter


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""

    if cap == "n/a":
        return 0

    value = float(cap[1:-1])
    denom = cap[-1:].lower()

    return value if denom == "m" else value * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""

    return round(
        sum(
            [
                _cap_str_to_mln_float(stock["cap"])
                for stock in data
                if stock["industry"] == industry
            ]
        ),
        2,
    )


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""

    return max(data, key=lambda x: _cap_str_to_mln_float(x["cap"]))["symbol"]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""

    count = Counter([stock["sector"] for stock in data if not stock["sector"] == "n/a"])

    return (count.most_common(1)[0][0], count.most_common()[-1][0])


print(_cap_str_to_mln_float("n/a"))  # 0
print(_cap_str_to_mln_float("$100.45M"))  # 100.45
print(_cap_str_to_mln_float("$20.9B"))  # 20900

print(get_industry_cap("Business Services"))  # 368853.27
print(get_industry_cap("Real Estate Investment Trusts"))  # 243295.36

print(get_stock_symbol_with_highest_cap())  # 'JNJ'

print(get_sectors_with_max_and_min_stocks())  # ('Finance', 'Transportation')

"""
Bite 129. Analyze Stock Data ☆
In this Bite we will answer some questions about stocks, using some JSON data obtained from the awesome Mockeroo fake data generator service.

Here is a snippet of the output you will parse (full output here):

  [{"id":1,"name":"Anworth Mortgage Asset  Corporation",
    "symbol":"ANH","industry":"Real Estate Investment Trusts",
    "sector":"Consumer Services","market":"NYSE","cap":"$600.57M"},
   {"id":2,"name":"DarioHealth Corp.",
   "symbol":"DRIO","industry":"Medical/Dental Instruments",
   "sector":"Health Care","market":"NASDAQ","cap":"$21.78M"},
   ... 998 more stocks ...
  ]
Complete the 4 functions below following the instructions in the docstrings. Good luck and keep calm and parse your Data in Python.
"""
