class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numberofislands=0
        def traverse(i,j):
            if(i<=-1 or j<=-1 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0"):
                return
            if(grid[i][j]==-1):
                return
            if(grid[i][j]=="1"):
                grid[i][j]=-1
            traverse(i+1,j)
            traverse(i,j+1)
            traverse(i,j-1)
            traverse(i-1,j)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    numberofislands+=1
                    traverse(i,j)
        return numberofislands