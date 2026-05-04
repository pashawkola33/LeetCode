# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# The overall run time complexity should be O(log(m + n)).
#
# Example:
#   Input: nums1 = [1,3], nums2 = [2]
#   Output: 2.0
#
# Time Complexity: O(log(min(m, n)))  — binary search on the smaller array
# Space Complexity: O(1)

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2      # partition index in nums1
            j = half_len - i        # partition index in nums2

            if i < m and nums2[j - 1] > nums1[i]:
                lo = i + 1          # move right in nums1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                hi = i - 1          # move left in nums1
            else:
                # Found the correct partition
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_left)

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0

        raise ValueError("Input arrays are not sorted or are invalid")


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    assert sol.findMedianSortedArrays([2], []) == 2.0
    print("All tests passed!")
