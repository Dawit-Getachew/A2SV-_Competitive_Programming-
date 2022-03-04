import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, res = Counter(nums), []
        priorityNum = [(count[x],x) for x in count]
        h.heapify(priorityNum)
        while len(priorityNum) != k:
            h.heappop(priorityNum)
        priorityNum = [y for x,y in priorityNum]
        return priorityNum