#!/usr/bin/python3
"""N-Queens Solver.

This script solves the N-Queens problem for a given integer N.
The N-Queens problem involves placing N queens on an N x N chessboard
in such a way that no two queens can attack each other. Queens can attack
other queens that are in the same row, column, or diagonal.

Usage:
    ./nqueens.py N

    - If N is less than 4, the program will print an error message and exit.
    - If N is not a number, the program will print an error message and exit.
    - If the number of arguments is incorrect, the program will
    print an error message and exit.

The program outputs each solution as a list of lists, where each inner list
represents the position of a queen in the format [row, column].

Example:
    $ ./nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""

import sys


def is_safe(position, queens):
    """Check if a queen can be placed at the given position.

    This function ensures that no two queens are attacking each other.
    It checks that the new queen does not conflict with any existing queens
    in the same column or diagonal.

    Args:
        position (list): The position [row, column] of the new queen.
        queens (list): The list of positions of already placed queens.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for row, col in queens:
        # Check column and diagonal conflicts
        diff = abs(row - position[0])
        if col == position[1] or diff == abs(col - position[1]):
            return False
    return True


def solve_nqueens(n, row=0, queens=[]):
    """Recursive function to solve the N-Queens problem.

    This function attempts to place queens row by row. For each row, it tries
    each column and recursively attempts to solve for the next row if
    the current placement is valid.
    When a full solution is found (when row == n), it
    prints the solution.

    Args:
        n (int): The size of the board (number of queens).
        row (int): The current row where we are placing a queen.
        queens (list): List of queen positions that form a partial solution.
    """
    if row == n:
        print(queens)
        return

    for col in range(n):
        position = [row, col]
        if is_safe(position, queens):
            # Place queen and move to the next row
            solve_nqueens(n, row + 1, queens + [position])


# Command-line argument handling
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Start solving the N-Queens problem
solve_nqueens(n)
