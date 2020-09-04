#!/usr/bin/env python3.8


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""

    lines = 0
    words = 0
    chars = 0

    with open(file_, "r") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)

    return f"{lines} {words} {chars} {file_}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))

