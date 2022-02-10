class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for i in range(len(nums)):
            if nums[i]==0:
                red += 1
            elif nums[i]==1:
                blue+=1
            else:
                white+=1
        if red!=0:
            for i in range(red):
                nums[i]=0
        if blue!=0:
            for i in range(red,red+blue):
                nums[i]=1
        if white!=0:
            for i in range(red+blue, red+blue+white):
                nums[i]=2
        return nums
    