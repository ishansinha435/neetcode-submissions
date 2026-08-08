class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, [], 0, 0, n)
        return res
    
    def backtrack(self, res, stack, o, c, n):
        if o == c == n:
            res.append(''.join(stack))
            return

        if o < n:
            stack.append('(')
            self.backtrack(res, stack, o + 1, c, n)
            stack.pop()
            
        if c < o:
            stack.append(')')
            self.backtrack(res, stack, o, c + 1, n)
            stack.pop()