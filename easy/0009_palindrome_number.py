# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# An integer is a palindrome when it reads the same backward as forward.
#
# Example:
#   Input: x = 121
#   Output: true
#
# Time Complexity: O(log n)  — we process half the digits
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # x == reversed_half  for even-length numbers
        # x == reversed_half // 10  for odd-length numbers (middle digit ignored)
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False
    assert sol.isPalindrome(0) is True
    assert sol.isPalindrome(1221) is True
    print("All tests passed!")
