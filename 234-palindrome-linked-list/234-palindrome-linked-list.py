# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = first_half= head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_
        if fast:
            slow = slow.next
        while prev and prev.val == slow.val:
            prev, slow = prev.next, slow.next
        return prev is None
        
        