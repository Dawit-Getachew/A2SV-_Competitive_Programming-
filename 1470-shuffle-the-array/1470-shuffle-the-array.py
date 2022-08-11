class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = []
        for i, s in zip(nums[:n], nums[n:]):
            final.append(i)
            final.append(s)
        return final