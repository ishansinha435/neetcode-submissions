class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, paren = [], []

        def backtrack(o, c):
            if o == c == n:
                res.append(''.join(paren))

            if o < n:
                paren.append('(')
                backtrack(o + 1, c)
                paren.pop()

            if c < o:
                paren.append(')')
                backtrack(o, c + 1)
                paren.pop()

        backtrack(0, 0)
        return res
