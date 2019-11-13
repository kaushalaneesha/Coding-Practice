"""
find-equilibrium-index-array

https://www.techiedelight.com/find-equilibrium-index-array/

"""
from typing import List


def fnd_equilibrium(arr: List[int]) -> List[int]:
    res = []
    sum_left, sum_right = 0, sum(arr)
    for i, num in enumerate(arr):
        if i > 0:
            sum_left += arr[i-1]
        sum_right -= num
        if sum_left == sum_right:
            res.append(i)
    return res


arr1 = [0, -3, 5, -4, -2, 3, 1, 0]
print(fnd_equilibrium(arr1))
