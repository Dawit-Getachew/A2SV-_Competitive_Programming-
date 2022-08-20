class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr, res = [], []
        for row in mat:
            for num in row:
                arr.append(num)
        if r * c != len(arr):
            return mat
        else:
            for row_index in range(r):
                res.append(arr[row_index * c : row_index * c + c])
            return res