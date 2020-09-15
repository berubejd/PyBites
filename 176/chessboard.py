#!/usr/bin/env python3.8
WHITE, BLACK = " ", "#"


def create_chessboard(size: int = 8) -> None:
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for rows in range(size):
        row = f"{WHITE}{BLACK}" * int(size / 2)
        print(row if rows % 2 == 0 else row[::-1])


create_chessboard(3)
