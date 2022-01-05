class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=list(map(lambda x: x*x,nums))
        nums.sort()
        return nums