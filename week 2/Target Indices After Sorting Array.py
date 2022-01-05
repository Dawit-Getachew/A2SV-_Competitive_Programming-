class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        num=[]
        for i in nums:
            if i != target:
                num.append(i)
                break
        num.append(target)
        return num