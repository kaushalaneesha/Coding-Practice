"""
In array of size n, containing numbers 1 to n. Find duplicate number
"""
from typing import List


def find_duplicate(arr: List[int]) -> int:
    for i, elem in enumerate(arr):


# Test case
a = [1, 4, 3, 4]
print(find_duplicate(a))
a = []
print(find_duplicate(a))
a = [6, 5, 4, 3, 2, 2]
print(find_duplicate(a))
a = [8, 7, 6, 5, 1, 2, 3, 8]
print(find_duplicate(a))