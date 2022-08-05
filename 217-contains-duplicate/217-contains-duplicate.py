class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count  =  Counter(nums).most_common()
        return True if count[0][1] > 1 else False