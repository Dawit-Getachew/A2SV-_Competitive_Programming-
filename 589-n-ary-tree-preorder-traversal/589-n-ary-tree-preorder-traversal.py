"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        stack, output = [root], []
        
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            stack.extend(curr.children[::-1])
            
        return output