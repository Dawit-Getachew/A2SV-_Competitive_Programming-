class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        min_price = [(1 << 24)] * (k + 1)
        max_profit = [0] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                temp = price - max_profit[i-1]
                if temp < min_price[i]: 
                    min_price[i] = temp 
                temp = price - min_price[i]
                if temp > max_profit[i]:
                    max_profit[i] = temp
        return max_profit[k]