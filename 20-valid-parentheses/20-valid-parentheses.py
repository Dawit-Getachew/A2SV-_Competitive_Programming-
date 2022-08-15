class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def push(item):
            stack.append(item)
        def Remove(stack):
            if stack:
                stack.pop()
            return
        def peak(stack):
            if stack:
                return stack[-1]
        newS = {"(","[","{"}
        for i in s:
            if i in newS:
                stack.append(i)
            elif i == ")" and peak(stack) == "(":
                Remove(stack)
            elif i == "]" and peak(stack) == "[":
                Remove(stack)
            elif i == "}" and peak(stack) == "{":
                Remove(stack)
            else:
                return False
        return False if len(stack) != 0 else True
        
        
            