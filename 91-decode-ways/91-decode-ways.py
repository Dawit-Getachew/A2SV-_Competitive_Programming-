class Solution:
    def numDecodings(self, s: str) -> int:
        dp2 = dp = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            dp = 0
            if s[i] != "0":
                if int(s[i:i + 2]) <= 26:
                    dp = dp1 + dp2
                else:
                    dp = dp1
            dp2, dp1 = dp1, dp
        return dp