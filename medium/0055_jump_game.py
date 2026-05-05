# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Difficulty: Medium
#
# You are given an integer array nums. You are initially positioned at the first
# index of the array, and each element in the array represents your maximum jump
# length at that position. Return true if you can reach the last index, or false
# otherwise.
#
# Example:
#   Input: nums = [2,3,1,1,4]
#   Output: true
#
# Time Complexity: O(n)  — greedy
# Space Complexity: O(1)

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0]) is True
    assert sol.canJump([2, 0, 0]) is True
    print("All tests passed!")
