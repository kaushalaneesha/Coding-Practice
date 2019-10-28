"""
Given an arbirary string, write an algorithm that partitions the string into
substring such that a) Each substring is a palindrome
b) number of palindromes are minimum
"""


def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


print(is_palindrome("a"))
