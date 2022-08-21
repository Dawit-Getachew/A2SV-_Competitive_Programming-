class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = sum(nums)
        res = (n*(n+1))//2
        if res == Sum:
            return 0
        else:
            return res - Sum