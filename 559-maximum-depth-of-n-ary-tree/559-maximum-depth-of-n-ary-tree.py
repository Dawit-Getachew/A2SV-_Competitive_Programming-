"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution: 
    def recur(self, root):
        if not root:
            return 0
        depth = 0
        if not root.children:
            return 1
        for child in root.children:
            depth = max(depth, self.recur(child))
        return depth + 1
    def maxDepth(self, root: 'Node') -> int:
        return self.recur(root)
        