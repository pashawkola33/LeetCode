# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Difficulty: Medium
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers
# sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
#
# Example:
#   Input: candidates = [2,3,6,7], target = 7
#   Output: [[2,2,3],[7]]
#
# Time Complexity: O(n^(t/m + 1)) where t = target, m = min candidate
# Space Complexity: O(t/m)

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, current: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()

        candidates.sort()
        backtrack(0, [], target)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.combinationSum([2, 3, 6, 7], 7)) == sorted([[2, 2, 3], [7]])
    assert sorted(sol.combinationSum([2, 3, 5], 8)) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert sol.combinationSum([2], 1) == []
    print("All tests passed!")
