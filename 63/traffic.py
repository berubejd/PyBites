#!/usr/bin/env python3.8

from collections import namedtuple
from itertools import cycle, islice
from time import sleep

from pprint import pprint as pp

State = namedtuple('State', 'color command timeout')


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""

    light = {'red': {'command': 'Stop', 'timeout':2}, 'green': {'command': 'Go', 'timeout': 2}, 'amber': {'command': 'Caution', 'timeout': 0.5}}

    for color in cycle(light):
        yield State(color, light[color]['command'], light[color]['timeout'])


if __name__ == '__main__':
    # print a sample of 10 states if run as standalone program
    # for state in islice(traffic_light(), 10):
    #     print(f'{state.command}! The light is {state.color}')
    #     sleep(state.timeout)

    pp(list(islice(traffic_light(), 10)))

"""
color - command - timeout
red - Stop - 2
green - Go - 2
amber - Caution - 0.5
"""
