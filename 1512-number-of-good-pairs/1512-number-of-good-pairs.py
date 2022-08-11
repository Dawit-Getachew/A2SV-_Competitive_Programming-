class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        col = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            col[nums[i]] += 1
        for i in col:
            if col[i]>=2:
                n = col[i]
                count += n*(n-1)//2
        return count
            