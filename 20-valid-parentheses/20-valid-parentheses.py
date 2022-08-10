class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def push(stack, inp):
            stack.append(inp)
        def pop (stack):
            if len(stack) == 0:
                return
            else:
                stack.pop()
        def peak(stack):
            if len(stack) == 0:
                return
            return stack[-1]
        opening = "({["
        closing = ")}]"
        for i in s:
            if i in opening:
                push(stack, i)
            elif i in closing and len(stack)!=0:
                if i == ")" and peak(stack) == "(":
                    pop(stack)
                elif i == "}" and peak(stack) == "{":
                    pop(stack)
                elif i == "]" and peak(stack) == "[":
                    pop(stack)
                else:
                    return False
            else:
                return False
        return len(stack) == 0