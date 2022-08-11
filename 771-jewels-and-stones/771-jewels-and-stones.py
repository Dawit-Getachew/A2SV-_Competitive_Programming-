class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jew = set(jewels)
        for i in stones:
            if i in jew:
                count+=1
        return count