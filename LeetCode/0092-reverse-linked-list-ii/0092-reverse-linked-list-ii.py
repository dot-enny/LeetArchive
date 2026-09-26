# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(-1, head)
        left_prev, curr = dummy, head
        for i in range(left - 1):
            left_prev, curr = curr, curr.next

        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next