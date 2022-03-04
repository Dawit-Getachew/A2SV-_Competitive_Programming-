import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        priorityNum = []
        res = []
        for n in count:
            priorityNum.append((-count[n], n))
        h.heapify(priorityNum)
        for i in range(k):
            res.append(h.heappop(priorityNum)[1])
        return res