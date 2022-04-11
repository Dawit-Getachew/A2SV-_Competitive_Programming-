class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n =  len(nums)-1
        nums.sort()
        result = nums[-1] - nums[0]
        for i in range(n):
            result = min(result, max(nums[-1] - k, nums[i] + k) - min(nums[0] + k, nums[i + 1] - k))
        return result