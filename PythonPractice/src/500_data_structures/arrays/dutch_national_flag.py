"""
Sort an array containing 0’s, 1’s and 2’s (Dutch national flag problem)
"""
from typing import List


def dutch_national_flag(arr: List[int]) -> None:
    one_count, two_count, zero_index = 0, 0, 0
    for _, num in enumerate(arr):
        if num == 0:
            arr[zero_index] = 0
            zero_index += 1
        elif num == 1:
            one_count += 1
        else:
            two_count += 1
    while one_count > 0:
        arr[zero_index] = 1
        one_count -= 1
        zero_index += 1
    while two_count > 0:
        arr[zero_index] = 2
        two_count -= 1
        zero_index += 1


arr = [0, 1, 2, 1, 0, 0, 2, 1]
dutch_national_flag(arr)
print(arr)

arr = [0, 0, 0, 0, 0]
dutch_national_flag(arr)
print(arr)
