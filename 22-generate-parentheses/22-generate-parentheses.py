class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[[] * (n+1) for j in range(n+1)] for i in range(n+2)]
        dp[1][1].append("(")
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i-1>j:
                    continue
                for k in dp[i-1][j]:
                    dp[i][j].append(k + ")")
                for k in dp[i][j-1]:
                    dp[i][j].append(k + "(")
        return dp[len(dp) - 1][len(dp[0]) - 1]