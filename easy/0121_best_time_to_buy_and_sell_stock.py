# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
#
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day. You want to maximize your profit by choosing a single day to
# buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
#
# Example:
#   Input: prices = [7,1,5,3,6,4]
#   Output: 5
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    print("All tests passed!")
