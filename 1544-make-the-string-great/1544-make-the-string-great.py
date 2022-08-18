class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1,len(s)):
            if stack and stack[-1] != s[i] and (stack[-1] == s[i].lower() or stack[-1] == s[i].upper()):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)