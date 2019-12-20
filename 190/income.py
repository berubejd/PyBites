#!/usr/bin/env python3.8

import os
from pathlib import Path
from urllib.request import urlretrieve

from collections import defaultdict
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/countries.xml", countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    income_dict = defaultdict(list)

    ns = {"wb": "http://www.worldbank.org"}

    data = ET.parse(xml)
    root = data.getroot()

    for country in root.findall("wb:country", ns):
        country_name = country.find("wb:name", ns).text
        income_level = country.find("wb:incomeLevel", ns).text

        income_dict[income_level].append(country_name)

    return income_dict


print(get_income_distribution())

"""
Bite 190. Parse income distribution from Latin America XML ☆
In this Bite you are going to parse some Latin American countries in xml, specifically the output of api.worldbank.org/V2/country?region=LCN which
we stored here. It's already saved for you in the countries temp file.

Complete get_income_distribution by reading in this file, parsing its XML and returning a dict of keys = wb:incomeLevel and values = lists of
country names (wb:name). defaultdict is a convenient data structure to use here. See also the tests for the expected return.

Good luck and code more Python!
"""
