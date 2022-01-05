class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        small=[]
        for i in range(len(nums)):
            counter=0
            for j in nums:
                if nums[i]>j:
                    counter+=1
            small.append(counter)
        return small