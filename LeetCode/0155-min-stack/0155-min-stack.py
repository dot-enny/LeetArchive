class MinStack:

    def __init__(self):
        self.s = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.s.append(val)
        if val < self.min: self.min = val

    def pop(self) -> None:
        val = self.s.pop()
        if val == self.min:
            self.min = float('inf')
            for n in self.s:
                if n < self.min:
                    self.min = n

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()