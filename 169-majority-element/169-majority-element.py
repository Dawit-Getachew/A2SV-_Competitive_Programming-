class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d =  defaultdict(int)
        n =  int(len(nums))/2
        for i in range(len(nums)):
            d[nums[i]] += 1
            if d[nums[i]]>n:
                return nums[i]
            