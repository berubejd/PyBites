#!/usr/bin/env python3.8

IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names: list) -> list:
    filtered = []

    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue

        if name.startswith(QUIT_CHAR):
            break

        if any(char.isdigit() for char in name):
            continue

        filtered.append(name)

        if len(filtered) >= MAX_NAMES:
            break

    return filtered


print(filter_names(["12", "bas"]))  # []
print(filter_names(["tim", "ana", "quinton"]))  # ['tim', 'ana']
print(
    filter_names(["tim", "amber", "ana", "cindy", "sara", "molly", "henry"])
)  # ['tim', 'amber', 'ana', 'cindy', 'sara']

