"""
Find groups of anagrams in a list. Assuming M words of length n
Approach 1
- Check if every pair is anagrams
- Complexity M square * nlogn

Approach 2
- Find a fingerprint of each word, like in this case, we can have a frequency
vector
Complexity : O(n)

- hashmap with fingerprint as the key. Add all anagrams to the same key
Complexity 0(nm)
"""

# Approach 1
# Find if two strings are anagrams
# Complexity: 0(nlogn)
from typing import List


def is_anagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    word1_list = sorted([ch for ch in word1])
    word2_list = sorted([ch for ch in word2])
    return word1_list == word2_list


def find_anagram_groups(words: List[str]) -> List[List[str]]:
    word_map = {}
    for word in words:
        word_frequency = [0] * 26
        for ch in word:
            word_frequency[ord(ch) - ord('a')] += 1
        if word_map.get(tuple(word_frequency)):
            word_map[tuple(word_frequency)].append(word)
        else:
            word_map[tuple(word_frequency)] = [word]
    return [v for k, v in word_map.items()]


print(is_anagram("fat", "act"))

print(find_anagram_groups(["cat", "bat", "rat", "act", "tab", "art"]))
