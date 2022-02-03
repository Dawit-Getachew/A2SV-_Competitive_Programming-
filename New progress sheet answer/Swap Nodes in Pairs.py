# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=curr= ListNode()
        while head and head.next:
            next_head =head.next.next
            node.next=head.next
            head.next.next=head
            node=head
            head=next_head
        node.next=head
        return curr.next