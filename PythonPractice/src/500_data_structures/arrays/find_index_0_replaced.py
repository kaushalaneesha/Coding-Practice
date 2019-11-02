"""
Find 0 to be replaced to find maximum length subsequence of continuous ones.
"""
from typing import List


def find_index_of_zero(arr: List[int]) -> int:
    len_arr = len(arr)
    if len_arr == 0:
        return -1
    elif len_arr == 1:
        if arr[0] == 1:
            return -1
        else:
            return 0
    count = 0
    arr1 = [0] * len_arr
    arr2 = [0] * len_arr
    for i, num in enumerate(arr):
        if num == 0:
            arr1[i] = 0
            count = 0
        else:
            count += 1
            arr1[i] = count
    count = 0
    for i in range(len_arr - 1, -1, -1):
        if arr[i] == 0:
            arr2[i] = 0
            count = 0
        else:
            count += 1
            arr2[i] = count
    max_len = 0
    zero_index = -1
    for i, num in enumerate(arr):
        if i == 0:
            if arr2[i + 1] > max_len:
                max_len = arr2[i + 1]
                zero_index = i
        elif i == len_arr - 1:
            if arr2[i - 1] > max_len:
                max_len = arr2[i - 1]
                zero_index = i
        elif arr1[i - 1] + arr2[i + 1] > max_len:
            max_len = arr1[i - 1] + arr2[i + 1]
            zero_index = i
    return zero_index


# Approach 2
def find_index_of_zero2(arr: List[int]) -> int:
    prev_index_zero, max_index_zero = -1, -1
    count, max_count = 0, 0
    for i, num in enumerate(arr):
        if num == 1:
            count += 1
        else:
            # reset count to number of 1s in left plus 1
            count = i - prev_index_zero
            prev_index_zero = i
        if max_count < count:
            max_count = count
            max_index_zero = prev_index_zero
    return max_index_zero


print(find_index_of_zero([0]))
print(find_index_of_zero([1]))
print(find_index_of_zero([]))
print(find_index_of_zero([0, 0, 1, 0, 1, 1, 1, 0, 1, 1]))


print(find_index_of_zero2([0]))
print(find_index_of_zero2([]))
print(find_index_of_zero2([0, 0, 1, 0, 1, 1, 1, 0, 1, 1]))
