# 51. N-Queens
# https://leetcode.com/problems/n-queens/
# Difficulty: Hard
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other. Given an integer n, return all
# distinct solutions to the n-queens puzzle.
#
# Example:
#   Input: n = 4
#   Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# Time Complexity: O(n!)
# Space Complexity: O(n)

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        pos_diag = set()   # (row + col)
        neg_diag = set()   # (row - col)
        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'
                backtrack(row + 1)
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    result_4 = sol.solveNQueens(4)
    assert len(result_4) == 2
    assert sorted(result_4) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])

    result_1 = sol.solveNQueens(1)
    assert result_1 == [["Q"]]

    result_8 = sol.solveNQueens(8)
    assert len(result_8) == 92
    print("All tests passed!")
