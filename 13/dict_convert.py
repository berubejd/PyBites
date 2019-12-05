#!/usr/bin/env python3.8

from typing import NamedTuple
from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Blog = namedtuple('Blog', ['name', 'founders', 'started', 'tags', 'location', 'site'])

def dict2nt(dict_: dict) -> NamedTuple:
    return Blog(**dict_)


def nt2json(nt: NamedTuple) -> json:
    def convert_dt(dt: datetime) -> str:
        return dt.__str__()

    return json.dumps(nt._asdict(), default=convert_dt)

new_nt = dict2nt(blog)
print(new_nt)
print(nt2json(new_nt))