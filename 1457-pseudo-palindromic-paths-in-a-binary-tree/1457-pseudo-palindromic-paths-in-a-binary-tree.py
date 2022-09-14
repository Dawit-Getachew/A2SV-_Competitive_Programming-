# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        parity_check= 0
        def helper(root, counter=parity_check):
            counter ^=(1<<root.val)
                           
            if not root.left and not root.right :
                if  counter&(counter-1)==0:
                    return 1
                else:
                    return 0
                
            
            leftpaths = rightpaths =0
            if root.left :
                leftpaths = helper(root.left,counter)
            
            if root.right :
                rightpaths = helper(root.right,counter)
        
            return leftpaths+rightpaths
    
        return helper(root)
