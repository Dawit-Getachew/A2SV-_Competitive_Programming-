class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[]
        nums.sort()
        for i in range(len(nums)//2):
            result.append(nums[i])
            result.append(nums[len(nums)-i-1])
        if len(nums)%2 !=0:
            result.append(nums[len(nums)//2])
        return result