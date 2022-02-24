class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lis=[]
        if k <= len(nums):
            for i in range(k):
                lis.append(nums.pop())
            for i in range(k):   
                nums.insert(0,lis[i])
        else:
            for i in range(k):
                nums.insert(0,nums.pop())