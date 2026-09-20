class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in hmap:
                stack.append(c)
            else:
                if not stack or c != hmap[stack.pop()]:
                    return False
        return not stack