# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        rever = None
        while slow:
            temp = slow.next
            slow.next = rever
            rever = slow
            slow = temp
        while rever:
            if rever.val != head.val:
                return False
            rever = rever.next
            head = head.next
        return True