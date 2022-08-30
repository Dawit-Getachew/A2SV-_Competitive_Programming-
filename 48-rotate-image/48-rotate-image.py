class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                if row == 0 and col == 0 or (row, col) in visited or (col, row) in visited:
                    continue
                a = matrix[row][col]
                b = matrix[col][row]
                matrix[row][col] = b
                matrix[col][row] = a
                visited.add((row, col))
                visited.add((col, row))
        for row in matrix:
            row.reverse()