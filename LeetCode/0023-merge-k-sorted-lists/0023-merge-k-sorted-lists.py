# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists: return None
        
        while len(lists) > 1:
            merged_lists = []
            n = len(lists)
            for i in range(0, n, 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < n else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        tail = dummy
        curr1, curr2 = l1, l2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        tail.next = curr1 if curr1 else curr2

        return dummy.next
            