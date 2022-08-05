class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d =  dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
                continue
            else:
                d[nums[i]] = 1
        k = len(nums)/2
        keys = list(d.keys())
        values = list(d.values())
        for i in range(len(values)):
            if values[i] > k:
                return keys[i]
                