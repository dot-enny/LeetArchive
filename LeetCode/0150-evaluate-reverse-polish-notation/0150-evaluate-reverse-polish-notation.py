class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                res = float('inf')
                if c == '+': res = left + right
                elif c == '-': res = left - right
                elif c == '*': res = left * right
                else:
                    res = math.trunc(left / right)
                stack.append(res)
                print(res)
        return int(stack.pop())

