class MinStack:

    def __init__(self):
        self.s = []
        self.prefix_min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not len(self.prefix_min):
            self.prefix_min.append(val)
        elif val < self.prefix_min[-1]:
            self.prefix_min.append(val)
        else:
            self.prefix_min.append(self.prefix_min[-1])

    def pop(self) -> None:
        val = self.s.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.prefix_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
