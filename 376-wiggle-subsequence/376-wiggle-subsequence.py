class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1
        if l == 2:
            return 1 if nums[0] == nums[1] else 2
        dif = []
        for i in range(1,l):
            if nums[i] == nums[i-1]:
                continue
            res = int((nums[i]-nums[i-1])/abs(nums[i]-nums[i-1]))
            if len(dif):
                if dif[-1] != res and res != 0:
                    dif.append(res)
            else:
                dif.append(res)
        return len(dif)+1
