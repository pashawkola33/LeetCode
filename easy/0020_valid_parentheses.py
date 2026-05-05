# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
#
# Example:
#   Input: s = "()[]{}"
#   Output: true
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    print("All tests passed!")
