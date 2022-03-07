import heapq as h
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in range(len(matrix)):
            temp= list(merge(temp,matrix[i]))
        return temp[k-1]