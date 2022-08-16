class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=sum(nums[:3])
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if(abs(summ-target)<abs(res-target)):
                    res=summ
                if summ<target:
                    l+=1
                else:
                    r-=1
        return res