class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i],nums[nz] = nums[nz], nums[i]
                nz += 1