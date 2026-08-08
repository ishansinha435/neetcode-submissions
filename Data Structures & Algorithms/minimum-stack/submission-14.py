class MinStack():

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, n):
        self.stack.append(n)
        self.min_stack.append(
            min(n, self.getMin()) if self.min_stack else n
        )

    def pop(self):
        if not self.stack:
            return Exception
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]