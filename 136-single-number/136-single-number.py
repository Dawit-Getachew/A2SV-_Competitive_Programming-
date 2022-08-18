class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for num in nums.keys():
            if nums[num] == 1:
                return num