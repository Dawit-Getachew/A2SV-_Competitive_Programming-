class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        start = {}
        ending = {}
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                ending[nums[i]] = i
                freq[nums[i]] = freq[nums[i]] + 1
            else:
                freq[nums[i]] = 1
                start[nums[i]] = i
                ending[nums[i]] = i
        req = 0
        val = 0
        res = 0
        for i in freq:
            if freq[i] > req:
                val = i
                req = freq[i]
                res = ending[i] - start[i] + 1
            elif freq[i] == req:
                if (ending[i] - start[i]) > 0 and (ending[i] - start[i])  < (ending[val] - start[val]):
                    res = ending[i] - start[i] + 1
                    
        return res