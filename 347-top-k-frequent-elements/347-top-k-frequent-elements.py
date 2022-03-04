import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        priorityNum = []
        res = []
        for n in count:
            priorityNum.append((count[n], n))
        for x,y in priorityNum:
            res.append((-x,y))
        h.heapify(res)
        priorityNum.clear()
        for i in range(k):
            priorityNum.append(h.heappop(res)[1])
        return priorityNum