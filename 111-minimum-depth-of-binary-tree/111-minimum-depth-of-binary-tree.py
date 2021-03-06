# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        counter = self.minDepth(root.left)
        counterRight = self.minDepth(root.right)
        if not root.left or not root.right:
            return 1 + counterRight + counter
        return 1 + min(counter, counterRight)