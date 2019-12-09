#!/usr/bin/env python3.8

import csv
import os
from urllib.request import urlretrieve

from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )

def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat = defaultdict(list)

    with open(BATTLE_DATA, "r") as fp:
        data = csv.DictReader(fp)

        for row in data:
            for k, v in row.items():
                if k == 'Attacker':
                    attacker = defeat[v]
                elif v == 'lose':
                    attacker.append(k)
                    
    return defeat


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    
    if not player1 in defeat_mapping or not player2 in defeat_mapping:
        raise ValueError('Invalid player type')

    if player2 in defeat_mapping[player1]:
        return player2
    elif player1 in defeat_mapping[player2]:
        return player1
    else:
        return 'Tie'

print(get_winner('Fire', 'Scissors'))