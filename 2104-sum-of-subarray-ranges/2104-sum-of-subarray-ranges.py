class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        Sum = 0
        for i in range(len(nums)):
            Min = nums[i]
            Max = nums[i]
            for j in range(i, len(nums)):
                Min = min(Min, nums[j])
                Max = max(Max, nums[j])
                Sum += Max - Min
        return Sum