class Solution:
    def countTexts(self, pk: str) -> int:
        MOD = 1e9+7        
        dp = [1]*(len(pk)+1)
        
        for i in range(1, len(pk)+1):
            dp[i] = dp[i-1]
            
            if i - 2 >= 0 and pk[i-1] == pk[i-2]:
                dp[i] += dp[i-2]
                dp[i] %= MOD
                
                if i-3 >= 0 and pk[i-2] == pk[i-3]:
                    dp[i] += dp[i-3]
                    dp[i] %= MOD
                    
                    if i-4 >= 0 and pk[i-3] == pk[i-4] and pk[i-1] in ('7', '9'):
                        dp[i] += dp[i-4]
                        dp[i] %= MOD
        
        
        return int(dp[-1])