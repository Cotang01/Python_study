"""
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
You can return the answer in any order.
"""


def two_sum_dict(nums: list[int], target: int) -> list[int]:
    nums_dict = {}
    n = len(nums)
    for i in range(n):
        comp = target - nums[i]
        if comp in nums_dict:
            return [nums_dict[comp], i]
        nums_dict[nums[i]] = i
    return []


def two_sum_2p(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    nums_enum = [(v, i) for i, v in enumerate(nums)]
    nums_enum.sort()
    while left < right:
        summa = nums_enum[left][0] + nums_enum[right][0]
        if summa == target:
            return [nums_enum[left][1], nums_enum[right][1]]
        elif summa > target:
            right -= 1
        else:
            left += 1
    return []
