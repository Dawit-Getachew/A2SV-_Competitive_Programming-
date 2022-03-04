import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, res = Counter(nums), []
        priorityNum = [(-count[x],x) for x in count]
        h.heapify(priorityNum)
        res = [h.heappop(priorityNum)[1] for i in range(k)]
        return res