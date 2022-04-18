class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        coolDown = sell = 0
        hold = float('-inf')        
        for dailyPrice in prices:
            prevCoolDown, prevSell, prevHold = coolDown, sell, hold
            coolDown = max(prevCoolDown, prevSell)
            sell = prevHold + dailyPrice
            hold = max(prevHold, prevCoolDown - dailyPrice)
        return max(sell, coolDown)