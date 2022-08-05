class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums).most_common()
        return count[0][0]
        