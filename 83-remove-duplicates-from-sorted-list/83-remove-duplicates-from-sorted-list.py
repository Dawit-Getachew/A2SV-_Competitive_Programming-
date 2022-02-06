# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, llist: Optional[ListNode]) -> Optional[ListNode]:
        if llist==None or llist.next==None:
            return llist
        head = llist;
        while llist.next:
           if llist.val != llist.next.val:
               llist = llist.next
           else:
               llist.next = llist.next.next
        return head