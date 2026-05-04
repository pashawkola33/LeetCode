# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# Return the maximum amount of water a container can store.
#
# Example:
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#
# Time Complexity: O(n)  — two pointers
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
    assert sol.maxArea([1, 2, 1]) == 2
    print("All tests passed!")
