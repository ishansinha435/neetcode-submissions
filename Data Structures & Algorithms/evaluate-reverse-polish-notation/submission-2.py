class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                right = int(stack.pop())
                stack.append(int(stack.pop()) - right)
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                right = int(stack.pop())
                stack.append(int((int(stack.pop()) / right)))
            else:
                stack.append(token)
        return stack[0]
            
