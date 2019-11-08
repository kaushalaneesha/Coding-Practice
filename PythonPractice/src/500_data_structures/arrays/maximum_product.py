"""
Find the maximum product of two elements of an array

Approach 1: Find the 2 maximum positive elem of array and find 2 maximum abs
negative numbers.
Return max above two products, of two negative or two postive numbers.
"""
from typing import List


def maximum_product(arr: List[int]) -> int:
    max_pos, sec_pos, max_neg, sec_neg = 0, 0, 0, 0
    for i, elem in enumerate(arr):
        if elem >= max_pos:
            sec_pos = max_pos
            max_pos = elem
        elif elem >= sec_pos:
            sec_pos = elem
        elif elem < 0 and abs(elem) >= max_neg:
            sec_neg = max_neg
            max_neg = abs(elem)
        elif elem < 0 and abs(elem) >= sec_neg:
            sec_neg = abs(elem)
    return max(max_pos * sec_pos, max_neg * sec_neg)


print(maximum_product([-10, -3, 5, 6, -2, -50, 90]))
