#!/usr/bin/env python3.8
"""
Bite 283. Like there's no tomorrow? ☆
Ever have difficulty remembering what today's date is?

How about tomorrow's?

I know I do...  Help me out by completing the tomorrow() function to return a date object with tomorrow's date.
"""
from datetime import date
from datetime import timedelta


def tomorrow(day=None) -> date:
    if not day:
        day = date.today()

    return day + timedelta(days=1)


print(tomorrow())
print(tomorrow(date(2020, 5, 1)))
