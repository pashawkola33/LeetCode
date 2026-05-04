# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
#
# Example:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
    print("All tests passed!")
