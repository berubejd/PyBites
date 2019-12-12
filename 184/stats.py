#!/usr/bin/env python3.8

from csv import DictReader
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)

from collections import Counter


class BiteStats:

    def _load_data(self, data) -> list:
        
        with open(data, "r") as fp:
            reader = DictReader(fp)
            return [row for row in reader]

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(set([stat['bite'] for stat in self.rows]))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(set([stat['bite'] for stat in self.rows if stat['completed'] == 'True']))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(set([stat['user'] for stat in self.rows]))

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len(set([stat['user'] for stat in self.rows if stat['completed'] == 'True']))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        return Counter([stat['bite'] for stat in self.rows]).most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        return Counter([stat['user'] for stat in self.rows if stat['completed'] == 'True']).most_common(1)[0][0]

test = BiteStats()
print(test.number_bites_accessed) # 176
print(test.number_bites_resolved) # 115
print(test.number_users_active) # 114
print(test.number_users_solving_bites) # 76
print(test.top_bite_by_number_of_clicks) # 101
print(test.top_user_by_bites_completed) # mcaberasu


'''
Bite 184. Analyze some Bite stats data ☆
In this Bite we will look at some Bite stats logs (usernames have been anonymized!):

$ head -5 bite_output_log.txt
bite,user,completed
102,ofancourt1,False
101,ofancourt1,False
29,emilham4,False
9,mfilshin6,False
Load in the data using csv's awesome DictReader storing the result in self.rows in the constructor (__init__). Next finish the 6 defined @property methods using the loaded in data. Each property returns a single value. Check out the docstrings and tests for more info.

Good luck and keep calm and code in Python!
'''
