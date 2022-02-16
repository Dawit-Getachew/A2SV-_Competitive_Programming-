class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr=0
        for i in range(len(nums)):
            if nums[i]==0:
                i+=1
            else:
                nums[ptr],nums[i]=nums[i],nums[ptr]
                ptr+=1
                i+=1