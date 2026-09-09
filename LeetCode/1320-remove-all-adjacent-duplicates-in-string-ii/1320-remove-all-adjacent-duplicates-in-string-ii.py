class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stores [char, current_consecutive_count] pairs
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        res = [c * s for c, s in stack]
        return ''.join(res)