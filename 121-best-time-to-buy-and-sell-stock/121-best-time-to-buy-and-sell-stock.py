class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left  = prices[0]
        for right in prices:
            if left < right:
                profit = max(profit, right - left)
            else: left = right
        return profit