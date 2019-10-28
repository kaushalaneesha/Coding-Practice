"""
Find maximum length sub-array having equal number of 0’s and 1’s
"""
from typing import List


def equal_0_and_1(arr: List[int]) -> List[int]:
    max_len, curr_sum = 0, 0
    ending_index = -1
    sum_map = {0: -1}
    for i, num in enumerate(arr):
        curr_sum += num if num == 1 else -1
        if sum_map.get(curr_sum) and max_len < i - sum_map.get(curr_sum):
            max_len = i - sum_map.get(curr_sum)
            ending_index = i
        else:
            sum_map[curr_sum] = i
    print(max_len)
    print(ending_index)
    return arr[ending_index - max_len + 1: ending_index + 1]


print(equal_0_and_1([0, 0, 1, 0, 1, 0, 0]))
