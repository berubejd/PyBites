#!/usr/bin/env python3.8

message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""

    seperator = "|"

    msg_split = message.split('\n')
    msg_joined = seperator.join(msg_split)

    return msg_joined

print(split_in_columns())
