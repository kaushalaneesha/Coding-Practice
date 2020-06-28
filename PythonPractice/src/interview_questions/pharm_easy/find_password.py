"""
Find password of a given string where password is the length of smallest substring which maximum distinct characters

Eg:
Input:
abcda

Ouput:
4

Input:
aabcdbfgtx

Output:
9

"""
import collections


def smallest_substring(S):
    len_S = len(S)
    unique_char = collections.defaultdict(lambda: 0)
    for s in S:
        unique_char[s] += 1
    distinct_char_count = len(unique_char)
    # If all characters are distinct return the length of the string as output
    if distinct_char_count == len_S:
        return S
    j, start, start_index, min_len = 0, 0, -1, 99999999
    curr_count = collections.defaultdict(lambda: 0)
    count = 0
    for i, s in enumerate(S):
        curr_count[s] += 1

        if curr_count[s] == 1:
            count += 1

        if count == distinct_char_count:
            while curr_count[S[start]] > 1:
                # if curr_count[S[start]] > 1:
                curr_count[S[start]] -= 1
                start += 1

            # update window size
            len_window = i - start + 1
            if len_window < min_len:
                min_len = len_window
                start_index = start

    return S[start_index: start_index + min_len]


input_str = "aaaabbbbbaaaaba"
print(smallest_substring(input_str))


