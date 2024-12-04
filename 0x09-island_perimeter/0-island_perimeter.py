#!/usr/bin/python3
"""module that calculate the perimeter of the island"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    The grid is a rectangular list of lists, where:
        - 0 represents water.
        - 1 represents land.
    Assumptions:
        - The grid is completely surrounded by water.
        - There is exactly one island (no lakes or multiple islands).
        - The island is connected horizontally or vertically (not diagonally).

    Parameters:
        grid (list of list of int): The grid representing the map.

    Returns:
        int: The total perimeter of the island.
    """
    finished = []
    primer = 0

    def avilable(position, grid):
        """
        Determine the number of adjacent land cells and their positions.

        Parameters:
            position (tuple): The current cell position (row, column).
            grid (list of list of int): The grid representing the map.

        Returns:
            list: A list where:
                - The first element is the count of adjacent land cells.
                - The second element is a position list of these land cells.
        """
        row, column = position
        lis_row = [row, row, row - 1, row + 1]
        lis_column = [column - 1, column + 1, column, column]
        avl = 0
        avlpos = []
        for r, c in zip(lis_row, lis_column):
            if grid[r][c] == 1:
                avl += 1
                avlpos.append((r, c))
        return [avl, avlpos]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            if grid[i][j] == 1:
                first_point = (i, j)
                finished.append(first_point)
                break
        if finished:
            break

    temp = finished.copy()
    while temp:
        av = avilable(temp[0], grid)
        primer += (4 - av[0])
        for i in av[1]:
            if i not in finished:
                temp.append(i)
                finished.append(i)
        temp.pop(0)

    return primer
