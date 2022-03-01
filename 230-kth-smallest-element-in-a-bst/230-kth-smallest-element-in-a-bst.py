# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            arr.append(root.val)
            traverse(root.right)
            
        traverse(root)
        temp=arr[0]
        for i in range(k):
            if temp<arr[i]:
                temp=arr[i]
        return temp