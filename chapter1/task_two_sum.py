"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

OUTPUT:
Success
Runtime: 868 ms, faster than 28.02% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 10.00% of Python3 online submissions for Two Sum.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i, value in enumerate(nums):
        hash_table[i] = value

    for first_index, value in hash_table.items():
        if target - value in nums:
            second_index = nums.index(target - value)
            if first_index != second_index:
                return [first_index, second_index]


if __name__ == '__main__':
    two_sum([3, 2, 4], 6)
