class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack)==0:
                stack.append(char)
            elif char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
        