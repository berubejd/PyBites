#!/usr/bin/env python3.8

from math import ceil

STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10) -> str:
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""

    max_row_length = rows*2-1

    tree = []

    # Star
    tree.append(f'{STAR:^{max_row_length}}')

    # Tree
    for row in range(1, rows + 1):
        leaf = LEAF * (row * 2 - 1)
        tree.append(f'{leaf:^{max_row_length}}')

    # Trunk
    trunk_width = ceil(max_row_length / 2)

    if trunk_width % 2 == 0:
        trunk = TRUNK * (trunk_width + 1)
    else:
        trunk = TRUNK * trunk_width

    for _ in range(2):
        tree.append(f'{trunk:^{max_row_length}}')

    return '\n'.join(tree)

print(generate_improved_xmas_tree())

'''
In this Bite you have to complete generate_improved_xmas_tree that takes a rows arg (= number of rows with leafs). For each row you add a star, leafs and a trunk and center them nicely. This bite is an extension to Bite 119 with additional elements and some twists.

Elements of the tree:

STAR: Every tree has exactly one star at the top row.
LEAF: Every tree has row_number * 2 - 1 leafs per row.
TRUNK: Every tree has a trunk with a height of 2 and a width which is half of the largest leaf row.
However, the trunk should always be nicely centered by having the same number of empty spaces on both sides of the trunk. Therefore, you have to consider the width of the leaf rows and do some conditional rounding :)

The tree with default args should look like this:

         +
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
    |||||||||||
    |||||||||||
'''