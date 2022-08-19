# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        hash = {}
        curr = head
        while curr is not None:
            if curr in hash:
                return curr
            else:
                hash[curr] = True
            curr = curr.next
        return None
