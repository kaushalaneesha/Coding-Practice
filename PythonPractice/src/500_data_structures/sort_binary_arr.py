"""
Sort binary array in linear time
Approach: Use two pointers:
    i : keeps the index of current element
    zero_index: keeps the index of latest zero filled in the resultant array
First fill all the zeros by putting 0 at zero_index when arr[i] is 0
Then hard code all the remaining indexes to 1
"""
from typing import List


def sort_binary_arr(arr: List[int]) -> None:
    zero_index = 0
    for i, num in enumerate(arr):
        if num == 0:
            arr[zero_index] = 0
            zero_index += 1
    while zero_index < len(arr):
        arr[zero_index] = 1
        zero_index += 1


# arr = [0, 1,1, 0]
# arr = [0]
# arr = [1]
# arr = [1, 1, 1, 1]
arr = [1, 1, 1, 0, 0, 0, 0]
sort_binary_arr(arr)
print(arr)
