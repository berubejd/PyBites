#!/usr/bin/env python3.8

from itertools import combinations
from itertools import permutations

def friends_teams(friends: list, team_size: int = 2, order_does_matter: bool = False):
    if order_does_matter:
        return permutations(friends, team_size)
    else:
        return combinations(friends, team_size)


friends = 'Bob Dante Julian Martin'.split()

combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
print(len(combos)) # 6

combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
print(len(combos)) # 12

combos = list(friends_teams(friends, team_size=3, order_does_matter=False))
print(len(combos)) # 4