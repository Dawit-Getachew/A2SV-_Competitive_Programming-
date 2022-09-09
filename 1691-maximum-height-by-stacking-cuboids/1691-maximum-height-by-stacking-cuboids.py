class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for i in range(len(cuboids)):
            cuboids[i]=sorted(cuboids[i])
        cuboids=sorted(cuboids)    
        #print(cuboids) 
        
        dp=[0]*(len(cuboids))
        for i in range(0,len(cuboids)):
            dp[i]=cuboids[i][-1]
            
        for i in range(1,len(cuboids)):
            for j in range(i):
                if cuboids[i][0]>=cuboids[j][0] and cuboids[i][1]>=cuboids[j][1] and cuboids[i][2]>=cuboids[j][2] and dp[i]<dp[j]+cuboids[i][2]:
                    dp[i]=dp[j]+cuboids[i][2]
                    
        return max(dp)   