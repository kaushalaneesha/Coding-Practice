"""
15. Alternate high low
https://www.techiedelight.com/rearrange-the-array-with-alternate-high-and-low-elements/
"""
from typing import List
import random


def alternate_high_low(arr: List[int]) -> None:
    i = 1
    arr_len = len(arr)
    while i < arr_len:
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        if i < arr_len - 1 and arr[i + 1] > arr[i]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
        i += 2


a = [1, 2, 3, 4, 5, 6, 7]
alternate_high_low(a)
print(a)
a = [9, 6, 8, 3, 7]
alternate_high_low(a)
print(a)
a = [6, 9, 2, 5, 1, 4]
alternate_high_low(a)
print(a)
