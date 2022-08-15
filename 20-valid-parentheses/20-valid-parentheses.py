class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def push(item):
            stack.append(item)
        def Remove():
            if stack:
                stack.pop()
            return
        def peak():
            if stack:
                return stack[-1]
        newS = {"(","[","{"}
        for i in s:
            if i in newS:
                stack.append(i)
            elif i == ")" and peak() == "(":
                Remove()
            elif i == "]" and peak() == "[":
                Remove()
            elif i == "}" and peak() == "{":
                Remove()
            else:
                return False
        return False if len(stack) != 0 else True
        
        
            