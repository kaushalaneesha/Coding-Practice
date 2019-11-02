"""
Merge two sorted arrays of size m and and n, where m >= 0 and x[] has exactly
n vacant cells.
"""
from typing import List


def merge_arrays(arr1: List[int], arr2: List[int]) -> None:
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    k = len_arr1 - 1
    # move all zeros to the front
    for i in range(len_arr1 - 1, -1, -1):
        if arr1[i] != 0:
            arr1[k] = arr1[i]
            k -= 1
    # merge the arrays
    p = 0
    j = k + 1
    i = 0
    while i < len_arr2 and j < len_arr1:
        if arr1[j] < arr2[i]:
            arr1[p] = arr1[j]
            p += 1
            j += 1
        else:
            arr1[p] = arr2[i]
            p += 1
            i += 1
    # copy remaining elements
    while i < len_arr2:
        arr1[p] = arr2[i]
        p += 1
        i += 1
    while j < len_arr1:
        arr1[p] = arr1[j]
        p += 1
        j += 1


array_1 = [0, 2, 0, 3, 0, 5, 6, 0, 0]
array_2 = [1, 8, 9, 10, 15]
merge_arrays(array_1, array_2)
print(array_1)
