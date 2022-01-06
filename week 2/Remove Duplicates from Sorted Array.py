class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        num=set(nums)
        k=len(num)
        finalNum=list(num)
        finalNum.sort()
        for i in range(len(finalNum)):
            nums[i]=finalNum[i]
        return k