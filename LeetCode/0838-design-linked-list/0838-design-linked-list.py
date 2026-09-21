class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.len = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index: return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next: self.tail = new_node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if index == self.len: self.addAtTail(val)
        else:
            curr = self.head
            i = 0
            while i < index and curr:
                curr = curr.next
                i += 1
            if curr:
                new_node.next = curr.next
                curr.next = new_node
                self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        if curr and curr.next:
            if self.tail == curr.next: self.tail = curr
            curr.next = curr.next.next
            self.len -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)