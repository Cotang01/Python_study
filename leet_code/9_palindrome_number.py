"""
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""


def is_palindrome(n: int) -> bool:
    if n < 0:
        return False
    else:
        n = str(n)
        left = 0
        right = len(n) - 1
        while left < right and left != right:
            if n[left] != n[right]:
                return False
            else:
                left += 1
                right -= 1
        return True