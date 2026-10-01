class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if stack and c in close_to_open:
                if close_to_open[c] != stack.pop(): return False
            else: stack.append(c)

        return not len(stack)