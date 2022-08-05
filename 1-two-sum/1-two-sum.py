class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = dict()
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dicti:
                return [dicti[compliment], i]
            dicti[nums[i]] = i
        return []