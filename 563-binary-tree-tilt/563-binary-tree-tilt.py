# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.Sum = 0
        def helper(root) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            left = helper(root.left)
            right = helper(root.right)
            self.Sum += abs(left-right)
            return left + right + root.val
            
        helper(root)
        return self.Sum