"""
Print all sub-arrays with 0 sum
"""
from typing import List


# Approach 1: Check if the sum of array from (i to j ) is zero or not
# where i goes from 0 to length of array. j goes from i to length of array
def print_subarray_zero(arr: List[int]) -> List[int]:
    for i, num in enumerate(arr):
        sum_elem = 0
        for j in range(i, len(arr)):
            sum_elem += arr[j]
            if sum_elem == 0:
                return arr[i: j + 1]
    return []


# print(print_subarray_zero([4, -2, 3, -1]))


# Approach 1: keep a hash set of sum of elements seen till now. If the sum
# appears again it means we have found a sub array of length 0
def print_subarray_zero2(arr: List[int]) -> List[List[int]]:
    res = []
    sum_elem = 0
    sum_set = {0: [-1]}
    for i, num in enumerate(arr):
        sum_elem += num
        key_elem = sum_set.get(sum_elem)
        if key_elem:
            for val in key_elem:
                res.append(arr[val + 1:i+1])
            sum_set[sum_elem].append(i)
        else:
            sum_set[sum_elem] = [i]
    return res


print(print_subarray_zero2([4, -2, 3, -1, 0, -4]))
print(print_subarray_zero2([4, 2, -3, -1, 0, 4]))
print(print_subarray_zero2([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]))
