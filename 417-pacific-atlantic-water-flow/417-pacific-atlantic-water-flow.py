class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or r < 0 or r == rows or c < 0 or c == cols or prevHeight > heights[r][c]:
                return

            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for j in range(cols):
            dfs(0, j, pac, heights[0][j])
            dfs(rows-1, j, atl, heights[rows-1][j])

        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atl, heights[i][cols-1])

        res = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res