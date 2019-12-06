#!/usr/bin/env python3.8
'''
Write a simple Promo class. Its constructor receives a name str and expires datetime.
Add a property called expired which returns a boolean value indicating whether the promo has expired or not.
Checkout the tests and datetime module for more info. Have fun!
'''

from datetime import datetime, timedelta

NOW = datetime.now()


class Promo(object):
    def __init__(self, name: str, expires: datetime):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return NOW > self.expires


past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo('twitter', past_time)
print(twitter_promo.expired) # True


future_date = NOW + timedelta(days=1)
newsletter_promo = Promo('newsletter', future_date)
print(newsletter_promo.expired) # False
