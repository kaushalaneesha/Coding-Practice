"""
Move zeros to end while maintaining the order

https://www.techiedelight.com/move-zeros-present-array-end/
"""
from typing import List


def move_zeros_to_end(arr: List[int]) -> None:
    slow, fast = 0, 0
    arr_len = len(arr)
    # Fill non zeros
    while fast < arr_len:
        if arr[fast] != 0:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    # Fill zeros
    while slow < arr_len:
        arr[slow] = 0
        slow += 1


arr1 = [6, 0, 8, 2, 3, 0, 4, 0, 1]
move_zeros_to_end(arr1)
print(arr1)

