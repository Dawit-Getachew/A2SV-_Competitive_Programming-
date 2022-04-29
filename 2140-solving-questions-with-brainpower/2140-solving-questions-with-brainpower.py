class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]*(len(questions)+1)
        for i in range(len(questions)-1, -1, -1):
            if i + questions[i][1] + 1 >= len(questions):
                dp[i] = max(questions[i][0], dp[i+1])
            else:
                dp[i] = max(dp[i + questions[i][1] + 1] + questions[i][0], dp[i+1])
        return dp[0]