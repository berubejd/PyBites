#!/usr/bin/env python3.8

from datetime import datetime
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates() -> datetime:
    from datetime import timedelta

    date = PYBITES_BORN
    
    while True:
        new_date = date + timedelta(days=100)

        anni = PYBITES_BORN + timedelta(days=(int((date - PYBITES_BORN).total_seconds()/(60 * 60 * 24 * 365) + 1 ) * 365))
        if anni > date and anni < new_date:
            yield anni

        yield new_date

        date = new_date

gen = gen_special_pybites_dates()
dates = list(islice(gen, 5))
print(dates)