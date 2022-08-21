"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res  = []
        def dfs(node):
            if not node:
                return None
            res.append(node.val)
            for nd in node.children:
                dfs(nd)
        dfs(root)
        return res