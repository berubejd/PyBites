#!/usr/bin/env python3.8

squares = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 0]]

sparse = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

empty = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

bad_map = [[]]

circles = [
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0],
]

sea = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
]

def count_islands(grid: list, debug: bool = False) -> int:
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """

    islands = 0

    for row_ptr, row in enumerate(grid):
        for cell_ptr, cell in enumerate(row):
            if cell == 1:
                if debug:
                    print("Found land.  Exploring!")

                if mark_islands(row_ptr, cell_ptr, grid):
                    if debug:
                        print("Discovered new land!")
                        print()

                    islands += 1
                else:
                    if debug:
                        print("False alarm.  We've found this before.")
                        print()

    return islands


def mark_islands(
    i: int, j: int, grid: list, new_island: bool = True, debug: bool = False
) -> bool:
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    if debug:
        print(f"Entered MARK: [{i}, {j}] = {grid[i][j]}")

    # Continue search if this is land, too
    if grid[i][j] == 1:
        # I am land so check the row below
        new_row = i + 1
        new_cell = j - 1

        # If there are rows below, continue down
        if new_row < len(grid):
            new_island = mark_islands(new_row, j, grid, new_island)

        # If there are more cells in this row, continue to the previous cell
        if new_cell >= 0:
            new_island = mark_islands(i, new_cell, grid, new_island)

        if debug:
            print("Marking this new land")

        grid[i][j] = "#"

    # Found that this is an existing island
    elif grid[i][j] == "#":
        if debug:
            print("Found existing land, exitting")

        return False

    if debug:
        print(f"Exitting MARK. This {'is still' if new_island else 'is NOT'} new land.")

    return new_island


print(count_islands(squares, True))  # 2
print(count_islands(sparse, True))  # 5
print(count_islands(empty, True))  # 0
print(count_islands(bad_map, True))  # 0
print(count_islands(circles, True))  # 1
print(count_islands(sea, True))  # 4

""" 
Bite 263. Count the number of islands in a grid ☆
You are tasked with counting the amount of islands in a 2D matrix / grid.

Islands are represented by 1s, oceans by 0. If the 1s are connected either horizontally 
or vertically (not diagonally), then they count as one island. You can assume a grid has 
a limited size up to 10x10. Try to make the search / count of number of islands as 
efficient as possible. If no islands are found, just return 0.

The goal is to find how many islands there are in the ocean, regardless of its size.

    Examples:

    ###### Example 1
    grid = [[1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0]]

    expected: 4 islands

    (top left island has size 5; top right = 2, bottom left = 2, bottom right = 1)
       
    ###### Example 2

    grid = [[1, 0, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 1]]
"""
