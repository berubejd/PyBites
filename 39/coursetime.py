#!/usr/bin/env python3.8

from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    all_times = []

    with open(COURSE_TIMES) as fp:
        for line in fp.read().splitlines():
            line = line.strip()

            m = re.search(r"(\d+:\d+)", line)
            if m:
                all_times.append(m.group())

    return all_times


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total = 0

    for item in timestamps:
        mins, secs = item.split(":")
        total += int(mins) * 60 + int(secs)

    return str(timedelta(seconds=total))


timestamps = get_all_timestamps()
print(calc_total_course_duration(timestamps))

"""
Bite 39. Calculate the total duration of a course ☆
In this Bite you read in a text file with course times (MM:SS) per video.

You extract these and calculate the total course duration in HH:MM:SS.

See the docstrings and tests for more details.

Have fun and we hope you learn a thing or two.

Trivia: in honor of our Code Challenges Pilot: this was the exercise we used to test the waters when we started out :)
"""
