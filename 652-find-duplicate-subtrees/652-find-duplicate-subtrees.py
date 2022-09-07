# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        dup = []
        def find(root):
            if root is None:    
                return "#"                      
            l = find(root.left)
            r = find(root.right)
            k = str(root.val) + "." + l + "." + r + "." 
            seen[k] += 1
            if seen[k] == 2:
                dup.append(root)
            return k                                   
        find(root)
        return dup