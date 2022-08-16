class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res=[0]
        s=sum(nums)
        for i in range(len(nums)):
            if res[-1]==s-nums[i]:
                return i
            else:
                res.append(res[-1]+nums[i])
                s=s-nums[i]
        return -1