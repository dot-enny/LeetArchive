# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(-1, head)
        prev, curr = dummy, dummy
        
        while n > 0 and curr.next: 
            curr = curr.next
            n -= 1
        while curr.next:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next

        return dummy.next

        left.next = left.next.next
        
        return dummy.next