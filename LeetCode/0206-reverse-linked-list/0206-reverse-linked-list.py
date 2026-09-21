# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes.reverse()
        n = len(nodes)
        for i, node in enumerate(nodes):
            node.next = nodes[i + 1] if (i + 1) < n else None
        return nodes[0] if n else head