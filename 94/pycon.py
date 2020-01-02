#!/usr/bin/env python3.8

from collections import namedtuple
import os
import pickle
import urllib.request

# prework
# download pickle file and store it in a tmp file
pkl_file = "pycon_videos.pkl"
data = f"https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}"
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.join(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple("Video", "id title duration metrics")

import re

def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, "rb") as fp:
        return pickle.load(fp)


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(videos, key=lambda x: int(x.metrics["viewCount"]), reverse=True)


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    return sorted(
        videos,
        key=lambda x: (int(x.metrics["likeCount"]) - int(x.metrics["dislikeCount"]))
        / int(x.metrics["viewCount"]),
        reverse=True,
    )


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [video for video in videos if "H" in video.duration]


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    video_list = []

    for video in videos:
        if not "H" in video.duration:
            m = re.search(r"(\d{2})M", video.duration)

            if int(m.group(1)) < 24:
                video_list.append(video)

    return video_list


pycon_data = load_pycon_data()

print(get_talks_lt_twentyfour_min(pycon_data)[:5])

"""
Bite 94. Parse PyCon talk data from YouTube ☆
PyCon2018 was awesome! But you clearly had to choose the whole time, so much was going on!

In this Bite we parsed all the talks from the PyCon 2018 YT channel and stored them into a list of Video namedtuples. This nested data structure is stored in a pickle file. The data looks like this:

[Video(id='T-TwcmT6Rcw',
             title='Raymond Hettinger - Dataclasses:  The code generator ...',
             duration='PT45M8S',
             metrics={'viewCount': '6047', 'likeCount': '139', 'dislikeCount': '2',
                              'favoriteCount': '0', 'commentCount': '14'}),
 Video(id='duvZ-2UK0fc', title='Ned Batchelder .... same attributes ...),
 Video(id='GBQAKldqgZs', title='Kenneth Reitz ....same attributes ...),
 ... same Video namedtuples ...]
See the full data dump here (note this is a snapshot as of today = 23rd of May 2018, the numbers will change, but we want static data for this Bite so we can run tests against your code).

Now the exercise: complete the 5 functions below, parsing this data set. See the docstrings and the tests for more info...

Have fun and keep calm and code in Python!
"""
