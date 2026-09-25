# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        curr1, curr2 = l1, l2
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            sum = carry + val1 + val2
            if sum > 9: 
                sum = str(sum)
                carry = int(sum[0])
                sum = int(sum[1])
            else: carry = 0
            curr.next = ListNode(sum)
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
            curr = curr.next
        if carry: curr.next = ListNode(carry)
        return dummy.next