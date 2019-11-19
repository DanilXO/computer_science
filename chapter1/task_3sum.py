"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

OUTPUT:
"""
from itertools import combinations
from typing import List


def three_sum(nums: List[int]) -> List[int]:
    hashmap = {}
    for i, value in enumerate(nums):
        hashmap[i] = value
        target = -value
        for first_index, value in hashmap.items():
            if target - value in nums:
                second_index = nums.index(target - value)
                if first_index != second_index:
                    return [first_index, second_index]


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
