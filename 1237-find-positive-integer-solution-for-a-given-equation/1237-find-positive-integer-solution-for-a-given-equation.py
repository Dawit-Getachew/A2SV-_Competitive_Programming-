"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        first, last = 1, 1000
        res = []
        def binarySearch(x,left,right):
            if left > right:
                return -1
            mid  = left + (right - left)//2
            temp = customfunction.f(x, mid)
            if temp == z:
                res.append([x, mid])
            elif temp > z:
                binarySearch(x, left, mid-1)
            elif temp < z:
                 binarySearch(x,mid+1, right)
        for i in range(1,1000):
            binarySearch(i, first, last)
        return res