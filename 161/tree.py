#!/usr/bin/env python3.8

import os
from pathlib import Path


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    number_of_directories = 0
    number_of_files = 0

    directory = Path(directory)

    for item in directory.iterdir():
        if item.is_dir():
            dirs, files = count_dirs_and_files(item)

            number_of_directories += dirs + 1
            number_of_files += files

        else:
            number_of_files += 1

    return number_of_directories, number_of_files


print(count_dirs_and_files("/home/berubejd/Python/PyBites/16"))

"""
16
├── gendates.py
├── gendates.pyc
├── __pycache__
│   ├── gendates.cpython-38.pyc
│   ├── test_gendates.cpython-27-PYTEST.pyc
│   └── test_gendates.cpython-38-pytest-5.2.2.pyc
├── .pytest_cache
│   ├── CACHEDIR.TAG
│   ├── .gitignore
│   ├── README.md
│   └── v
│       └── cache
│           ├── lastfailed
│           ├── nodeids
│           └── stepwise
└── test_gendates.py

4 directories, 12 files
"""
