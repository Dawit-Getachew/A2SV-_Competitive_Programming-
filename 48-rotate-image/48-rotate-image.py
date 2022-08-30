class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        y_dim = len(matrix)
        x_dim = len(matrix[0])
        for i in range(0, y_dim):
            for j in range(i, x_dim):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, y_dim):
            matrix[i].reverse()