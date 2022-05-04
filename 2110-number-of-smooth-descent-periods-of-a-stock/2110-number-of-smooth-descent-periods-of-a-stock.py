class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        curr = result = 1
        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i-1]:
                curr += 1
            else:
                curr = 1
            result += curr            
        return result