# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSum(self, root, targetSum):
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum==0
        return self.checkSum(root.right, targetSum) or self.checkSum(root.left, targetSum)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkSum(root, targetSum)