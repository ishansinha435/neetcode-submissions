class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        for c in tokens:
            if c in ops:
                r = stack.pop()
                l = stack.pop()
                if c == '+':
                    stack.append(l + r)
                elif c == '-':
                    stack.append(l - r)
                elif c == '*':
                    stack.append(l * r)
                elif c == '/':
                    res = l // r if l / r >= 0 else math.ceil(l / r)
                    stack.append(res)
                print(stack[-1])
            else:
                stack.append(int(c))
        return stack.pop()