class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counted =  Counter(nums)
        return sorted(counted.elements())