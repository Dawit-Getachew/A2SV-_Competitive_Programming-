# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        lis=[]
        while head:
            lis.append(head)
            head=head.next
        maxSum=0
        for i in range(1, len(lis)):
            Sum=lis[i-1].val+lis[len(lis)-i].val
            maxSum=Sum if maxSum<Sum else maxSum
        return maxSum