class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            com = target - nums[i]
            if( com in nums and nums.index(com) != i):
                return [i, nums.index(com)]
            