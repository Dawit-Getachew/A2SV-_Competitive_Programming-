import heapq as h

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
    def add(self, val: int) -> int:
        h.heapify(self.nums)
        h.heappush(self.nums, val)
        while len(self.nums) != self.k:
            h.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)