#!/usr/bin/env python3.8

pw4 = """
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
avar:x:1000:1000::/home/avar:/bin/bash
chad:x:1001:1001::/home/chad:/bin/bash
git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
"""

import re
from collections import defaultdict


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    pass_dict = defaultdict(str)

    for line in passwd.strip().splitlines():

        line = line.split(":")
        pass_dict[line[0]] = (
            re.sub(r"([,])(\1+)", r" ", line[4].rstrip(",")) or "unknown"
        )

    return pass_dict


print(get_users(pw4))

'''
Bite 257. Extract users dict from a multiline string ☆
A quick Bite to practice some string parsing extracting a users dict from a password 
file.

Complete get_users is how it works:

>>> from users import get_users
>>> pw = """
... postfix:x:108:112::/var/spool/postfix:/bin/false
... ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
... artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
... """
>>> get_users(pw)
{'postfix': 'unknown', 'ssh-rsa': 'unknown', 'artagnon': 'Ramkumar R Git GSOC'}

So keys are usernames, values are names. Note that commas inside the name get 
replace by a single space. Trailing commas (not in this example) get stripped off.

Have fun and keep calm and code in Python!
'''
