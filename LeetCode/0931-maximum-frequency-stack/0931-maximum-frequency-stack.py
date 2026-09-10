class FreqStack:

    def __init__(self):
        self.levels = defaultdict(list)
        self.max_freq = defaultdict()
        self.highest_level = 0

    def push(self, val: int) -> None:
        if val in self.max_freq: self.max_freq[val] += 1
        else: self.max_freq[val] = 1
        self.levels[self.max_freq[val]].append(val)
        self.highest_level = max(self.highest_level, self.max_freq[val])

    def pop(self) -> int:
        val = self.levels[self.highest_level].pop()
        self.max_freq[val] -= 1

        if not self.levels[self.highest_level]:
            self.highest_level -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()