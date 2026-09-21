# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # Base case: empty list or single node is already reversed
        if not head or not head.next: 
            return head

        # Subproblem: reverse everything after head
        new_head = self.reverseList(head.next)

        # Re-wire: point next node back to me, cut my old forward link
        head.next.next = head
        head.next = None

        return new_head