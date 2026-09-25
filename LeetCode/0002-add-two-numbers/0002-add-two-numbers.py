# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = carry + val1 + val2
            if sum > 9: 
                sum = str(sum)
                carry = int(sum[0])
                sum = int(sum[1])
            else: carry = 0
            curr.next = ListNode(sum)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        if carry: curr.next = ListNode(carry)
        return dummy.next
        
