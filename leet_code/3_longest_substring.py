"""
Given a string s, find the length of the longest substring without
repeating characters.
"""


def length_of_longest_substring(s: str) -> int:
    result = 0
    letters = {}
    start = 0
    for end in range(len(s)):
        if s[end] not in letters:
            result = max(result, end - start + 1)
        else:
            if letters[s[end]] < start:
                result = max(result, end - start + 1)
            else:
                start = letters[s[end]] + 1
        letters[s[end]] = end
    return result
