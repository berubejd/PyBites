#!/usr/bin/env python3.8

from enum import Enum

orig = [1, 2, 3, 4]
same = orig
ordered = orig[:]
unordered = orig[::-1]
deduped = orig[:] + [1, 3, 4, 4]
not_same = [4, 5, 6]


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""

    if list1 is list2:
        return Equality.SAME_REFERENCE

    if list1 == list2:
        return Equality.SAME_ORDERED

    list1.sort()
    list2.sort()

    if list1 == list2:
        return Equality.SAME_UNORDERED

    if set(list1) == set(list2):
        return Equality.SAME_UNORDERED_DEDUPED

    return Equality.NO_EQUALITY


print(check_equality(orig, same))  # Equality.SAME_REFERENCE
print(check_equality(orig, ordered))  # Equality.SAME_ORDERED
print(check_equality(orig, unordered))  # Equality.SAME_UNORDERED
print(check_equality(orig, deduped))  # Equality.SAME_UNORDERED_DEDUPED
print(check_equality(orig, not_same))  # Equality.NO_EQUALITY
