class Solution:
    def dfs(self, image: List[List[int]], sr: int, sc: int, newColor: int, DIR: List[List[int]], startColor: int) -> List[List[int]]:
        image[sr][sc] = newColor
        visited = set()
        visited.add((sr,sc))
        
        
        for direction in DIR:
            newRow, newCol = sr + direction[0], sc + direction[1]
            if not self.checkSize(newRow, newCol, len(image), len(image[0])) or (newRow, newCol) in visited or image[newRow][newCol] != startColor:
                continue
            
            self.dfs(image, newRow, newCol, newColor, DIR, startColor)
            
            
        return image
        
    def checkSize(self, row: int, col: int, rowSize: int, colSize: int) -> bool:
        return True if 0 <= row < rowSize and 0 <= col < colSize else False
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        startColor = image[sr][sc]
        image[sr][sc] = newColor
        DIR = [[0,1], [1,0], [0,-1], [-1,0]]
        
        image = self.dfs(image, sr, sc, newColor, DIR, startColor)
        return image
        