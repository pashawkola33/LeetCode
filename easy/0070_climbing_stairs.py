# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
#
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Example:
#   Input: n = 3
#   Output: 3  (1+1+1, 1+2, 2+1)
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr


if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(4) == 5
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(10) == 89
    print("All tests passed!")
