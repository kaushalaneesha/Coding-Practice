"""
Merge two sorted arrays in place, without using extra space
"""
from typing import List


def merge_arrays(arr1: List[int], arr2: List[int]) -> None:
    len_2 = len(arr2)
    if len_2 < 1:
        return
    for i, num in enumerate(arr1):
        if num > arr2[0]:
            arr2[0], arr1[i] = arr1[i], arr2[0]
            first = arr2[0]
            # for k in range(len_2, -1, -1):
            k = 1
            while k < len_2 and arr2[k] < first:
                arr2[k-1] = arr2[k]
                k += 1
            arr2[k-1] = first


array_1 = [1, 4, 7, 8, 10]
array_2 = [2, 3, 9]
merge_arrays(array_1, array_2)
print(array_1)
print(array_2)
