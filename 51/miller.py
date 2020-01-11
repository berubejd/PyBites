#!/usr/bin/env python3.8

from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    seconds = (PY2_DEATH_DT - start_date).total_seconds()

    return round(seconds / 3600, 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    m_sec_min = 3679200
    seconds = (PY2_DEATH_DT - start_date).total_seconds()
    
    return round(seconds/m_sec_min, 2)


print(py2_earth_hours_left())
print(py2_miller_min_left())

"""
Bite 51. When does Python 2 die on Planet Miller? ☆
Imagine you landed on Planet Miller (from the movie Interstellar) where 1 hour takes 7 Earth years (known as the gravitational time dilation effect - see here if interested).

Given a fixed start date BITE_CREATED_DT (26th of Feb 2018) calculate:

How many hours Python 2 has left on Planet Earth
How many minutes Python 2 has left on Planet Miller
As per pythonclock.org Python 2.7 will retire on 1st of Jan 2020 (after this date you can still do this Bite because we work a fixed start date.)

Have fun and keep calm and code in Python!
"""