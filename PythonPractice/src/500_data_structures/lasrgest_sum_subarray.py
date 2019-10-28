"""
Find largest sub-array formed by consecutive integers
"""
from typing import List


def largest_sum(arr: List[int]) -> List[int]:
    mi, mj, ci, cj, curr_sum, max_sum = -1, -1, 0, 0, 0, 0
    for i, num in enumerate(arr):
        curr_sum += num
        cj += 1
        if curr_sum < 0:
            curr_sum = 0
            ci = i + 1
            cj = i + 1
        elif max_sum < curr_sum:
            max_sum = curr_sum
            mi = ci
            mj = cj
    return arr[mi: mj]


print(largest_sum([-6, 3, 2, -8, 6]))
print(largest_sum([]))
