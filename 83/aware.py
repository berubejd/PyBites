#!/usr/bin/env python3.8

from datetime import datetime
from pytz import timezone, utc

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""

    aware_dt = naive_utc_dt.replace(tzinfo=utc)
    return (aware_dt.astimezone(AUSTRALIA), aware_dt.astimezone(SPAIN))


naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
print(
    what_time_lives_pybites(naive_utc_dt)
)  # (datetime.datetime(2018, 4, 28, 8, 55, tzinfo=<DstTzInfo 'Australia/Sydney' AEST+10:00:00 STD>), datetime.datetime(2018, 4, 28, 0, 55, tzinfo=<DstTzInfo 'Europe/Madrid' CEST+2:00:00 DST>))
