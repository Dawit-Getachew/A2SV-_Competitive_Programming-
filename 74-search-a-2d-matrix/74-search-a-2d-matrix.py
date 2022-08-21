class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix):
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = (n * m) - 1
        
        while low <= high:
            mid = int(low + (high - low) / 2)
            
            if matrix[int(mid / m)][int(mid % m)] == target:
                return True
            elif matrix[int(mid / m)][int(mid % m)] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False