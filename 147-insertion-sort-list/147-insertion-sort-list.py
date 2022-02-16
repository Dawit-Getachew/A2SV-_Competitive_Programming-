# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        start = head
        while start:
            arr.append(start.val)
            start = start.next
        
        def insertionSort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i-1
                while j >= 0 and key < arr[j] :
                        arr[j + 1] = arr[j]
                        j -= 1
                arr[j + 1] = key
        insertionSort(arr)
        i=0
        start=head
        while start:
            start.val=arr[i]
            i+=1
            start=start.next
        return head