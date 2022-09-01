# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodRoots = []
        def dfs(root, maxNum):
            if not root:
                return 0    
            res = 1 if root.val >= maxNum else 0
            maxNum = max(maxNum, root.val)
            res+= dfs(root.left, maxNum)  
            res+= dfs(root.right, maxNum)
            return res
        return dfs(root,root.val)