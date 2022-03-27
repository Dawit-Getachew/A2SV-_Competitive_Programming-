class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag  = False
        low, high = 0, len(nums)-1
        for i in range(len(nums)):
            if target > nums[i]:
                low = i + 1
            elif target < nums [i]:
                high = i - 1
            elif target == nums[i]:
                return i
        if flag == False:
            return -1