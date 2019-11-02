"""
Check if a sub array exists with sum 0
"""
from typing import List


# Approach 1: Check if the sum of array from (i to j ) is zero or not
# where i goes from 0 to length of array. j goes from i to length of array
def check_sum_zero(arr: List[int]) -> bool:
    for i, num in enumerate(arr):
        if num == 0:
            return True
        sum_elem = 0
        for j in range(i, len(arr)):
            sum_elem += arr[j]
            if sum_elem == 0:
                return True
    return False


print(check_sum_zero([4, 9, -2, 3, -1]))


# Approach 1: keep a hash set of sum of elements seen till now. If the sum
# appears again it means we have found a sub array of length 0
def check_sum_zero2(arr: List[int]) -> bool:
    sumElem = 0
    sumSet = set([])
    sumSet.add(0)
    for i, num in enumerate(arr):
        sumElem += num
        if sumSet.__contains__(sumElem):
            return True
        else:
            sumSet.add(sumElem)
    return False


print(check_sum_zero2([4, 9, -2, 3, -1]))
