# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def rec(node, max_so_far):
            if not node:
                return 0
            if node.val >= max_so_far:
                return 1 + rec(node.left, node.val) + rec(node.right, node.val)
            return rec(node.left, max_so_far) + rec(node.right, max_so_far)
        
        return rec(root, -inf)
        