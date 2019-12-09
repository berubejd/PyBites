#!/usr/bin/env python3.8

def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
       
    max_row_length = rows*2-1

    # for row in range(1, rows+1):
    #     stars = '*' * (row * 2 - 1)
    #     print(f'{stars:^{max_row_length}}')

    return '\n'.join([f'{"*" * (row * 2 - 1):^{max_row_length}}' for row in range(1, rows+1)])

print(generate_xmas_tree(10))
