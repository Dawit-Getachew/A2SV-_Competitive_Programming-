class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = []
        for val in nums:
            s.append(val*val)
        return sorted(s)