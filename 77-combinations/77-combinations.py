class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] 
        def c(arr, lowerRange):
            if len(arr) == k: 
                res.append(arr[:])
                return
            
            for num in range(lowerRange, n+1):
                arr.append(num) 
                c(arr, num+1)
                arr.pop()
        c([], 1)
        return res