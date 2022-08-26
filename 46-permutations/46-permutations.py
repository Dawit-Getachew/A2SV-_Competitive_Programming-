class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for n in nums:
                new = nums.copy()
                new.remove(n) 
                ans = self.permute(new)
                for item in ans:
                    item.append(n)
                res.extend(ans)
            return res