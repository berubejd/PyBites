#!/usr/bin/env python3.8
"""
Bite 36. Having fun with *args and **kwargs ☆
Write a function called get_profile that takes:

a required name,
a required age,
one or more optional sports (args),
one or more optional awards (keyword args).
Add the following validations:

if age is not an int raise a ValueError,
if more than 5 sports are provided raise a ValueError.
Some examples how your function can be called (see also the TESTS tab):

get_profile('tim', 36)
get_profile('tim', 36, 'tennis', 'basketball')
get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis') 
The function should return a dict with all the args, like so:

get_profile('tim', 36) == {'name': 'tim', 'age': 36}  # some arg types
{'name': 'tim', 'age': 36, 'sports': ['basketball', 'tennis'], 'awards': {'champ': 'helped out team in crisis'}}  # all arg types
(args list to be sorted alphabetically)
We hope this gives you a good handle on Python's different types of function arguments. Enjoy!
"""


def get_profile(name, age, *sports, **awards):
    if not type(age) is int or len(sports) > 5:
        raise ValueError

    profile = {"name": name, "age": age}

    if sports:
        profile["sports"] = sorted(sports)

    if awards:
        profile["awards"] = awards

    return profile


print(get_profile("tim", 36))
print(get_profile("tim", 36, "tennis", "basketball"))
print(get_profile("tim", 36, "tennis", "basketball", champ="helped out team in crisis"))
