# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = []
        def helper(root):
            if not root:
                return
            if root.left and  root.left.left == root.left.right == None:
                stack.append(root.left.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return sum(stack)