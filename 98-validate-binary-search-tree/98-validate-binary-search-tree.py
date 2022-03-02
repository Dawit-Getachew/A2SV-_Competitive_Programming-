# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(node,bigger,smaller):
            if not node:
                return True
            if node.val >= bigger or node.val <= smaller:
                return False
            l = checker(node.left, node.val, smaller)
            r = checker(node.right, bigger, node.val)
            return l and r
        
        return checker(root, float('inf'), float('-inf'))