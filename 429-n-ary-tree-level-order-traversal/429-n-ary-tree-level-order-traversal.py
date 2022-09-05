"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(not root): return
        s = [root]
        ans = []
        i = 0
        while(s):
            ans.append([i.val for i in s])
            l = len(s)
            for _ in range(l):
                for child in s.pop(0).children:
                    s.append(child)
        return ans