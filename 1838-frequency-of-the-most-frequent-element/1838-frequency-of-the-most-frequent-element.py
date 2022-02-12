class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = res = 0
        Sum = 0
        while right < len(nums):
            Sum += nums[right]
            while nums[right]*(right-left+1)-Sum > k:
                Sum -= nums[left]
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res