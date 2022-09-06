# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==1:
            return [TreeNode(val=1)]

        self.mem =  { }
  
        def back_track(l, r):
            if (l,r) in self.mem:
                return self.mem[(l,r)]
            
            if l > r:
                return [None]
            elif l == r:
                return [TreeNode(val=l)]
                
            res=[]
            for i in range(l, r+1):
                lefts=back_track(l, i-1)
                rights=back_track(i+1, r)
                
                for lf in lefts:
                    for rt in rights:
                        curr_node = TreeNode(val=i, left=lf, right=rt)
                        res.append(curr_node)
                
            if (l,r) not in self.mem:
                    self.mem[(l,r)]= res
            return res
        
        back_track(1, n)
        
        return self.mem[(1, n)]