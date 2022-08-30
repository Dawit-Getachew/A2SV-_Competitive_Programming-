class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        for j in range(len_col-1, -1, -1):
            new_row = []
            for i in range(len_row-1, -1, -1):
                new_row.append(matrix[i][j])
                del matrix[i][j]
            matrix[j].extend(new_row)