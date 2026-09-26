# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        i, dummy = 1, ListNode(-1, head)
        prev, curr = dummy, head
        start = None

        while i <= right:
            temp = curr.next
            if i > left: 
                if curr.next != start: curr.next = prev
                else: curr.next = None
            elif i == left: start = prev
            
            prev = curr
            curr = temp
            i += 1
            
        start.next.next = curr
        start.next = prev

        return dummy.next