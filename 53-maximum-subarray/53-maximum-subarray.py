class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(curr_sum+num, num)
            max_sum = max(curr_sum, max_sum)
        return max_sum