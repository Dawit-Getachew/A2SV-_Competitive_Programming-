# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        val,nodePtr = list(), head
        while nodePtr:
            val.append(nodePtr.val)
            nodePtr = nodePtr.next
        if len(val) is not 1:
            left, right = 0, len(val)-1
            while left<right:
                head.val, head.next.val = val[left], val[right]
                left += 1
                right -= 1
                head = head.next.next
            if left==right and head is not None:
                head.val = val[left]