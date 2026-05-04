# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty string "".
#
# Example:
#   Input: s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"
#
# Time Complexity: O(m + n)  — sliding window
# Space Complexity: O(m + n)

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        have, required = 0, len(need)
        window = {}
        left = 0
        best_start, best_len = 0, float('inf')

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == required:
                # Update best window
                window_size = right - left + 1
                if window_size < best_len:
                    best_len = window_size
                    best_start = left
                # Shrink from left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        return s[best_start:best_start + best_len] if best_len != float('inf') else ""


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow("aa", "aa") == "aa"
    print("All tests passed!")
