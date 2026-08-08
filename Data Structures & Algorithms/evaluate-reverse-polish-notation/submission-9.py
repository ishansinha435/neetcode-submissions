class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            res = 0
            if(t == "+"):
                res = stack.pop() + stack.pop()
            if(t == "-"):
                back = stack.pop()
                res = stack.pop() - back
            if(t == "*"):
                res = stack.pop() * stack.pop()
            if(t == "/"):
                back = stack.pop()
                res = stack.pop() / back
                res = int(res)
            
            if t in "+-*/": 
                stack.append(res)
            else:
                stack.append(int(t))
            print(stack)
        return stack[-1]


        