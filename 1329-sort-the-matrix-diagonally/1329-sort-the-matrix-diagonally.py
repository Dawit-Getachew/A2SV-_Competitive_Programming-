from heapq import *
from collections import defaultdict as dd
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = dd(lambda:[])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                heappush(d[i-j], mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = heappop(d[i-j])
        return mat