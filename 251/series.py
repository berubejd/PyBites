#!/usr/bin/env python3.8

import string

import pandas as pd
import numpy as np


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    data = {"Fred": list(range(1, 6))}

    df = pd.DataFrame(data)

    return df["Fred"]


def float_series() -> pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    data = np.linspace(0, 1, 1001)

    return pd.Series(data)


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    data = {k: v for k, v in zip(string.ascii_lowercase, range(1, 27))}

    return pd.Series(data)


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    data = {k: v for v, k in zip(string.ascii_uppercase, range(101, 127))}

    return pd.Series(data)


print("Basic Series")
bs = basic_series()
print(bs.name)  # Fred
print(bs.dtype)  # int64
print(all(n in [1, 2, 3, 4, 5] for n in bs.values))  # True
print()

print("Float Series")
fs = float_series()
print(fs.dtype)  # float64
print(len(fs))  # 1001
print(fs.sum())  # 500.5
print()

print("Alpha Index Series")
ls = alpha_index_series()
print(ls.dtype)  # int64
print(len(ls))  # 26
print(sum(ls.values))  # 351
print(all(c in string.ascii_lowercase for c in ls.index))  # True
print()

print("Object Series")
os = object_values_series()
print(len(os))  # 26
print(all(c in string.ascii_uppercase for c in os.values))  # True
print(os[101])  # A
print(os[126])  # Z
print()


"""
Bite 251. Introducing Pandas Series ☆
Let's get started with Pandas! In case you are not aware of who, or what, 
pandas is, pandas is an open source, BSD-licensed library providing 
high-performance, easy-to-use data structures and data analysis tools for 
the Python programming language.

The two primary data structures in pandas are the Series and the DataFrame. 
The simplest way to visualise these two structures is to use an analogy 
with your favourite Spreadsheet application. Think of a pandas Series as 
Column A of Sheet 1 of your spreadsheet. Looking at the screen grab below 
it has 1 dimension (Column A) that represents the Series values, plus the 
row numbers which represent the indexes. A Dataframe is the whole 
spreadsheet, 2 dimensions or multiple columns, but more of that later.

This is what a Series looks like in a Spreadsheet.

pandas series

In a spreadsheet the row indexes typically start at 1 and the column names 
typically start at A. The Series called A above has four value [1, 2, 3, 4].

This is what a similar Series looks like in pandas:

>>> x
0    1
1    2
2    3
Name: Fred, dtype: int64

The pandas Series Python variable is named x. The default index, like all 
other Python objects, are zero-based so the index values are [0, 1, 2] and 
the series values are [1, 2, 3]. The sample x series shown is called Fred 
and all the series values are of type int64.

Creating Series
Now that you know everything that you need to know about pandas Series it's 
time for you to start creating some series of your own. In this Bite you are 
asked to complete a number of functions that each create a pandas Series. 
How you create each series is up to you but if you do your research you'll 
find that Series can be created from all different type of Python Objects:

1. Create a Series with values [1, 2, 3, 4, 5] of type int64, don't worry about 
the index but make Fred the name of the Series

2. Create a Series with values [0.000, 0.001, ... 0.999, 1.000] of type 
float64, don't worry about the index

3. Create a Series with values [1, 2, ... 25, 26] of type int64, and add an 
index with values [a, b, ... y, z] so index a = 1, b = 2 ... y = 25, z = 26

4. Create a Series with values [A, B, ... Y, Z] of type object, and add an 
index with values [101, 102, ... 125, 126] so index 101 = 'A', 102 = 'B' ... 
125 = 'Y', 126 = 'Z'

In the the next Bite we'll look at getting the values out of the Series in 
a useful manner.
"""
