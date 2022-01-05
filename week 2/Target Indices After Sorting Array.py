class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        num=[]
        for i in range(len(nums)):
            if nums[i]==target:
                num.append(i)
        return num