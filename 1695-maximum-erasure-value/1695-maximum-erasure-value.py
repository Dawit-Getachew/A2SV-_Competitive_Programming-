class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        lis = set()
        res = 0
        curr_sum = max_sum = left= 0
        for num in nums:
            while num in lis:
                curr_sum -= nums[left]
                lis.remove(nums[left])
                left += 1
            curr_sum += num
            lis.add(num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
                    
                