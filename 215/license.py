#!/usr/bin/env python3.8
import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    r = re.compile("^PB(-(\d|[A-Z]){8}){4}$")
    m = r.match(key)

    return True if m else False


print(validate_license("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"))  # True
print(validate_license("pb-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"))  # False
print(validate_license("bogus"))  # False
print(validate_license("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZ.."))  # False
print(validate_license("PB-F2WIMPR9-6ACLST1J-KD4579MN-0DGR9HQ5A"))  # False
