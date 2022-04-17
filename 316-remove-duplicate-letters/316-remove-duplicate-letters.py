class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for index, char in enumerate(s):
            if not stack:
                stack.append(char)
            elif char in stack:
                continue
            elif stack is not None:
                while stack and char < stack[-1]:
                    if stack[-1] in s[index + 1:]:
                        stack.pop()
                    else:
                        break
                stack.append(char)
        return ''.join(stack)