# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = iterator = 0
        node=head
        while head:
            counter+=1
            head=head.next
        while node:
            if iterator==(counter//2):
                return node
            iterator+=1
            node=node.next