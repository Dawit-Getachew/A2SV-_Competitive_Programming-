# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversed = []
        
        def traverse(r):
            if r is None:
                return
            traverse(r.left)
            traversed.append(r.val)
            traverse(r.right)
            
        traverse(root)
        
        for i in range(1, len(traversed)):
            if traversed[i] > traversed[i-1]:
                pass
            else:
                return False
        return True
        # if sorted(list(set(traversed))) == traversed:
        #     return True
        # else:
        #     return False