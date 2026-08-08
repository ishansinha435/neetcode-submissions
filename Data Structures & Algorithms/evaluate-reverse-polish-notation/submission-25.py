class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                r, l = stack.pop(), stack.pop()
                res = l // r if l / r >= 0 else math.ceil(l / r)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[0]