"""
Get the bricks that are not connected to the base

X XX
 X X
 X
 X

return : (0,0), (0,2), (0,3), (1,3)
"""
from typing import List


def get_non_connected_bricks(arr: List[List[int]], row: int, col: int) -> \
        List[tuple]:
    res = []
    for i in range(col):
        if arr[row - 1][i] == 1:
            arr[row - 1][i] = 2
            mark_connected(arr, row - 2, i, row, col)
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                res.append((i, j))
    return res


def mark_connected(arr: List[List[int]], row, col, total_row,
                   total_col) -> None:
    if 0 <= row < total_row and 0 <= col < total_col:
        if arr[row][col] == 2 or arr[row][col] == 0:
            return None
        else:
            arr[row][col] = 2
            mark_connected(arr, row - 1, col, total_row, total_col)
            mark_connected(arr, row + 1, col, total_row, total_col)
            mark_connected(arr, row, col - 1, total_row, total_col)
            mark_connected(arr, row, col + 1, total_row, total_col)


arr1 = [[1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]
print(get_non_connected_bricks(arr1, 4, 4))
