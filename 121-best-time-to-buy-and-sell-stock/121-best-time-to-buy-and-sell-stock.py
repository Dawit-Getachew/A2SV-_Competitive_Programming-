class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxPrice = float('inf'), 0
        for i in prices:
            minPrice = min(minPrice,i)
            change = i - minPrice
            maxPrice = max(maxPrice,change)
        return maxPrice