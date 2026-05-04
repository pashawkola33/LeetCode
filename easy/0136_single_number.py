# 136. Single Number
# https://leetcode.com/problems/single-number/
# Difficulty: Easy
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
# Example:
#   Input: nums = [4,1,2,1,2]
#   Output: 4
#
# Time Complexity: O(n)
# Space Complexity: O(1)  — XOR trick

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([1]) == 1
    print("All tests passed!")
