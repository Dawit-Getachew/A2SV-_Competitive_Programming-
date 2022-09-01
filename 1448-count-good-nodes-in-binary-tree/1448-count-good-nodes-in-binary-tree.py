# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk=[[root,root.val]]
        res=1
        while stk:
            temp=stk.pop()
            if temp[0].left:
                if temp[0].left.val>=temp[1]:
                    res+=1
                    stk.append([temp[0].left,temp[0].left.val])
                else:
                    stk.append([temp[0].left,temp[1]])
            if temp[0].right:
                if temp[0].right.val>=temp[1]:
                    res+=1
                    stk.append([temp[0].right,temp[0].right.val])
                else:
                    stk.append([temp[0].right,temp[1]])
        return res