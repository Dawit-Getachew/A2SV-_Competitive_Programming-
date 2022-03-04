import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        h.heapify(nums)
        nums = [-h.heappop(nums) for _ in range(k)]
        return nums[k-1]