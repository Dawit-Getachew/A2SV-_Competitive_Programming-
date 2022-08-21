"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return result