# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth, self.result = 0, None
        def helper(root, currRow):
            if root is None:
                return
            if currRow > self.depth:
                self.depth = currRow
                self.result = root.val
            helper(root.left, currRow+1)
            helper(root.right, currRow+1)
        helper(root, 1)
        return self.result