# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def dfs(r, row, col):
            d[col].append((row, r.val))
            if r.left: dfs(r.left, row+1, col-1)
            if r.right: dfs(r.right, row+1, col+1)
        dfs(root, 0, 0)
        return [[e for _, e in sorted(v)] for k, v in sorted(d.items())]