class Solution:
    def trap(self, height: List[int]) -> int:
        trapped=0
        i=0
        j=len(height)-1
        lmax=0
        rmax=0
        while i<=j:
            if height[i]<=rmax: 
                if height[i]>lmax:
                    lmax=height[i] 
                else:
                    trapped+=lmax-height[i]
                i+=1
            else:
                if height[j]>rmax: 
                    rmax=height[j]
                else:
                    trapped+=rmax-height[j]
                j-=1
        return trapped