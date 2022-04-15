class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = dict()
        def dfs(i,j):
            if i == len(triangle):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = triangle[i][j] + min(dfs(i+1,j) , dfs(i+1,j+1))
            return dp[(i,j)]
        return dfs(0,0)