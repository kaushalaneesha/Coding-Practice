"""
Find majority element.

https://www.techiedelight.com/find-majority-element-in-an-array-boyer-moore-majority-vote-algorithm/

"""
from typing import List


def find_majority(arr: List[int]) -> int:
    # Assuming -1 is not in the array
    count, candidate = 0, -1
    for num in arr:
        if count == 0:
            count += 1
            candidate = num
        else:
            if num == candidate:
                count += 1
            else:
                count -= 1
    # Validate if candidate is majority elem
    count_candidate = 0
    for num in arr:
        if num == candidate:
            count_candidate += 1

    if count_candidate > len(arr) / 2:
        return candidate
    else:
        return -1


arr1 = [8, 2, 7, 2, 2, 5, 2, 3, 1, 2, 2]
print(find_majority(arr1))
