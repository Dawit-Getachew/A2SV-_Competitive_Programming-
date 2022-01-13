class Solution:
    def isValid(self, s: str) -> bool:
        par=dict(('()', '[]', '{}'))
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif len(stack) == 0 or char != par[stack.pop()]:
                return False
        return len(stack) == 0

# class Solution:
#     def isValid(self, s: str) -> bool:
#         par=dict()
#         par["("]=')'
#         par['{']='}'
#         par['[']=']'
#         stack = []
#         for char in s:
#             if char in par.keys():
#                 stack.append(char)
#             elif len(stack) == 0 or char != par[stack.pop()]:
#                 return false
#         return len(stack) == 0