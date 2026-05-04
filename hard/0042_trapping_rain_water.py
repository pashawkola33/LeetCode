# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard
#
# Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it can trap after raining.
#
# Example:
#   Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6
#
# Time Complexity: O(n)  — two pointers
# Space Complexity: O(1)

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water


if __name__ == "__main__":
    sol = Solution()
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    assert sol.trap([]) == 0
    assert sol.trap([3, 0, 2, 0, 4]) == 7
    print("All tests passed!")
