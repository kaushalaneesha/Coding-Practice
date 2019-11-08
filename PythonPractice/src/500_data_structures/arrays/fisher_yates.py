"""
Shuffle an array
"""
from typing import List
import random


def shuffle(arr: List[int]) -> None:
    for i in range(len(arr) - 1, -1, -1):
        r = random.randint(0, i)
        # swap numbers
        arr[i], arr[r] = arr[r], arr[i]


arr = [1, 2, 3, 4, 5,  6, 7]
shuffle(arr)
print(arr)

