class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        wsum = 0
        minlen = math.inf
        
        for j in range(len(nums)):
            wsum += nums[j]
            while wsum >= target:
                minlen = min(minlen, j-i+1)
                wsum -= nums[i]
                i += 1
        if minlen == math.inf:
            return 0
        else:
            return minlen