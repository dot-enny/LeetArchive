"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randoms = { None: None }
        dummy = Node(-1)
        curr1, curr2 = head, dummy

        while curr1:
            new_node = Node(curr1.val)
            curr2.next = new_node
            curr2 = curr2.next
            randoms[curr1] = curr2
            curr1 = curr1.next
            
        curr1 = head
        while curr1:
            randoms[curr1].random = randoms[curr1.random]
            curr1 = curr1.next

        return dummy.next
