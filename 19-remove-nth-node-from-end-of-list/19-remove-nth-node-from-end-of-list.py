# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        counter=0
        while start:
            start=start.next
            counter+=1
        counter=counter-n
        start=head
        if counter==0:
            return start.next
        for i in range(counter):
            if i==counter-1:
                start.next=start.next.next
                return head
            start=start.next