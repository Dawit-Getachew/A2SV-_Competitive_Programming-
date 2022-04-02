# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Helper(self, root, depth):
        if not root:
            return None
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.result = root.val
        self.Helper(root.left, depth+1)
        self.Helper(root.right, depth+1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int: 
        self.result, self.maxDepth = root.val,0
        self.Helper(root,0)
        return self.result