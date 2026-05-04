# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
#
# There is an integer array nums sorted in ascending order (with distinct values)
# that is possibly rotated at an unknown pivot index. Given the array nums and an
# integer target, return the index of target if it is in nums, or -1 if it is not.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example:
#   Input: nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([1, 3], 3) == 1
    print("All tests passed!")
