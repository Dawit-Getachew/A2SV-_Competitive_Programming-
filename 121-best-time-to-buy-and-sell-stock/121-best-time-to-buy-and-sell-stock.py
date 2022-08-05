class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        minDiff = float('inf')
        maxDiff = 0
        for i in prices:
            minDiff = min(minDiff, i)
            change = i - minDiff
            diff = max(diff, change)
        return diff
        