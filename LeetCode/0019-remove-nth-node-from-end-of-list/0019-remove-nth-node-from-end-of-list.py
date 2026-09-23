# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(-1, head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left, right = left.next, right.next

        left.next = left.next.next
        
        return dummy.next