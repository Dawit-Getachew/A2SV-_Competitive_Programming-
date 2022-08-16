class Solution:        
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
            elif char == stack[-1][0]:
                stack[-1][1]+=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char,1])
                
        res = ""
        
        for char, count in stack:
            res = res + (char*count)
        return res