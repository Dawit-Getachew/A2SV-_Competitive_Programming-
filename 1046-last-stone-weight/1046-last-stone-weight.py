import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones)>1:
            tempOne = -1 * heapq.heappop(stones)
            tempTwo = -1 * heapq.heappop(stones) 
            if tempOne > tempTwo:
                heapq.heappush(stones, -1*(tempOne - tempTwo))
            elif tempOne == tempTwo:
                continue
        return 0 if len(stones) == 0 else -1 * stones[0]