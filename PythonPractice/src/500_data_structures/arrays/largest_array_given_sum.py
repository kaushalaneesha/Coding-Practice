"""
Given an array of integers find the maximum length sub array having the given
sum
"""
from typing import List


def given_sum_subarray(arr: List[int], total: int) -> List[int]:
    max_len, curr_sum = 0, 0
    ending_index = -1
    sum_map = {0: -1}
    for i, num in enumerate(arr):
        curr_sum += num
        if sum_map.get(curr_sum - total) and i - sum_map.get(curr_sum - total) > max_len:
            max_len = i - sum_map.get(curr_sum - total)
            ending_index = i
        else:
            if not sum_map.get(curr_sum):
                sum_map[curr_sum] = i
    print(max_len)
    print(ending_index)
    return arr[ending_index - max_len + 1: ending_index+1]


print(given_sum_subarray([5, 6, -5, 5, 3, 5, 3, 3, -2, 0], 8))
print(given_sum_subarray([-1, -1, 1, -1, 1, -1, -1], 0))


