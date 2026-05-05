# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Difficulty: Easy
#
# Given an integer array nums, find the subarray with the largest sum,
# and return its sum.
#
# Example:
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6  (subarray [4,-1,2,1])
#
# Time Complexity: O(n)  — Kadane's algorithm
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-1]) == -1
    print("All tests passed!")
