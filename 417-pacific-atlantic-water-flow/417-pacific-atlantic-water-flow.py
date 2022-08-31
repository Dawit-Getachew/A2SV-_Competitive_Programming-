class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, previous, visited):
            in_bounds = 0 <= row < n and 0 <= col < m

            if not in_bounds:
                return

            if (row, col) in visited:
                return

            if previous > heights[row][col]:
                return

            visited.add((row, col))
            dfs(row + 1, col, heights[row][col], visited)
            dfs(row - 1, col, heights[row][col], visited)
            dfs(row, col + 1, heights[row][col], visited)
            dfs(row, col - 1, heights[row][col], visited)

        for i in range(n):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, m-1, heights[i][m-1], atlantic)

        for j in range(m):
            dfs(0, j, heights[0][j], pacific)
            dfs(n-1, j, heights[n-1][j], atlantic)

        return [list(item) for item in pacific.intersection(atlantic)]