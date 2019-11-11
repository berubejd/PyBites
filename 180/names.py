#!/usr/bin/env python3.8

from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:

    import csv

    countries = defaultdict(list)

    for line in csv.DictReader(data.splitlines()):
        countries[line['country_code']].append(f"{line['first_name']} {line['last_name']}")

    return countries

print(group_names_by_country(data))
