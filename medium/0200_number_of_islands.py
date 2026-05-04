# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically.
#
# Example:
#   Input: grid = [["1","1","0","0","0"],
#                  ["1","1","0","0","0"],
#                  ["0","0","1","0","0"],
#                  ["0","0","0","1","1"]]
#   Output: 3
#
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)  — recursion stack

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert sol.numIslands(grid1) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert sol.numIslands(grid2) == 3
    print("All tests passed!")
