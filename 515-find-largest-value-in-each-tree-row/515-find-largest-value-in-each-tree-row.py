# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def helper(self, root, rowLevel):
            if not root:
                return
            if len(self.result) <= rowLevel:
                self.result.append(root.val)
            self.result[rowLevel] = max(self.result[rowLevel], root.val)
            self.helper(root.left, rowLevel + 1)
            self.helper(root.right, rowLevel + 1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root, 0)
        return self.result