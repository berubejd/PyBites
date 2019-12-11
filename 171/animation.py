#!/usr/bin/env python3.8

from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""

    total_time = 0
    
    for state in cycle(SPINNER_STATES):
        total_time += STATE_TRANSITION_TIME
        if total_time > seconds:
            print()
            break

        print(f"\r{state}", flush=True, end="")
        sleep(STATE_TRANSITION_TIME)


if __name__ == '__main__':
    spinner(1)

expected = SPINNER_STATES * 2
expected += SPINNER_STATES[:2]
print(''.join(expected))

# print(f"{state}", flush=True, end="")

'''
Bite 171. Make a terminal spinner animation ☆
In this Bite you will spice up your command line apps with a loader animation.

You will use itertools.cycle and sys.stdout to make the following terminal spinner animation:

Apart from the module imports we already defined SPINNER_STATES and STATE_TRANSITION_TIME = the amount of time to pause between states. Hopefully this will make it a bit easier.

One last hint is to look at how to flush terminal output so states you print to stdout don't get concatenated.

Good luck and keep calm and code in Python!
'''
