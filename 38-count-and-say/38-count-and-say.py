class Solution:
    def countAndSay(self, n: int) -> str:
        lookup = {1: "1"}
        def fun(n):
            if n in lookup:
                return lookup[n]
            else:
                val = fun(n-1)
                res = ""
                start = 0
                i = 1
                while i < len(val):
                    if val[i] != val[i-1]:
                        res+=str(i-start) + val[i-1]
                        start = i
                    i+=1
                res+=str(i-start) + val[-1]
                lookup[n] = res
                return res
        return fun(n) 