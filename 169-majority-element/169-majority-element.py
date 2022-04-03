class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for key, val in dic.items():
            if val > len(nums)//2:
                return key
        return