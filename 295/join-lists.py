#!/usr/bin/env python3.8
"""
Bite 295. Join lists ☆
Write a function that accepts a list of lists and joins them with a separator character, therefore flattening and separating.  

Examples:  

>>> join_lists([ ['a', 'b'], ['c'] ], '&')
['a', 'b', '&', 'c']
>>> join_lists([ ['a', 'b'], ['c'], ['d', 'e'] ], '+')
['a', 'b', '+', 'c', '+', 'd', 'e']
Note: Calling the function with an empty list should return None. 
"""
from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    new_list = []

    if not lst_of_lst:
        return None

    for lst in lst_of_lst:
        if new_list:
            new_list.append(sep)

        new_list.extend(lst)

    return new_list


print(join_lists([["a", "b"], ["c"], ["d", "e"]], "+"))
