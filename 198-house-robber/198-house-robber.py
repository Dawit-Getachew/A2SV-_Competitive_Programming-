class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            money = max(nums[i] + dp[-2], dp[-1])
            dp.append(money)
        return dp[-1]