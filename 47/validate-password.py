#!/usr/bin/env python3.8
"""
Bite 47. Write a new password field validator ☆
You know these Create a new password forms? They do a lot of checks to make sure you make a password that is hard to guess and you will surely forget.

In this Bite you will write a validator for such a form field.

Complete the validate_password function below. It takes a password str and validates that it:

is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
If the password matches all criteria the function should store the password in used_passwords and return True.

Have fun, keep calm and code in Python!
"""
import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):

    # Verify required lenght
    password_length = len(password)
    if not password_length >= 6 or not password_length <= 12:
        return False

    # Verify at least one digit
    if not any(map(str.isdigit, password)):
        return False

    # Verify at least two lower case
    lower_case = 0
    for index in range(password_length):
        char = password[index]
        if type(char) == str and char in string.ascii_lowercase:
            lower_case += 1

    if not lower_case >= 2:
        return False

    # Verify at least one upper case
    if not any(map(str.isupper, password)):
        return False

    # Verify at least one punctuation
    if not any(map(lambda x: x in PUNCTUATION_CHARS, password)):
        return False

    # Verify not in used password list
    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True


print(validate_password("12345aAa!"))
print(validate_password("12345aAa!"))