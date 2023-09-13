"""
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""


def is_palindrome_str(x: int) -> bool:
    if x < 0:
        return False
    else:
        n = str(x)
        left = 0
        right = len(n) - 1
        while left < right and left != right:
            if n[left] != n[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


def is_palindrome_int(x: int) -> bool:
    if x < 0:
        return False
    else:
        x_buffer = x
        comparable = 0
        while x > 0:
            comparable = comparable * 10 + x % 10
            x //= 10
        return x_buffer == comparable
