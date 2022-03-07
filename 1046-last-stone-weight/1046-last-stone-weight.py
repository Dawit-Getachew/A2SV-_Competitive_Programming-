class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            if stones[-1] > stones[-2]:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()
            elif stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
        return 0 if len(stones) == 0 else stones[0]