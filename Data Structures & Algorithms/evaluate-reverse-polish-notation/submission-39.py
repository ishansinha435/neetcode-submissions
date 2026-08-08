class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                r, l = stack.pop(), stack.pop()
                print(int(l // r))
                stack.append(int(l / r))
            else:
                stack.append(int(t))
        return stack[-1]