class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        temp = []
        max = 0
        for i in range(0,len(nums),2):
            temp.append([nums[i],nums[i+1]])
        for j in range(len(temp)):
            max += min(temp[j][0], temp[j][1])
        return max
        