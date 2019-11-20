#!/usr/bin/env python3.8

def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    """Return key of int parts made up of int characters per part which should be upper case letters and numbers"""
    import secrets
    import string

    return '-'.join(''.join(secrets.choice(string.ascii_uppercase + string.digits) for token in range(chars_per_part)) for part in range(parts))

print(gen_key())
print(gen_key(parts=3, chars_per_part=4))
