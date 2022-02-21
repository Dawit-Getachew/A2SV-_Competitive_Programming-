class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, curr = [], ""
        for Str in s:
            if Str=='(':
                stack.append(curr)
                curr=""
            elif Str==')':
                curr=curr[::-1]
                curr=stack.pop()+curr
            else:
                curr+=Str
        return curr