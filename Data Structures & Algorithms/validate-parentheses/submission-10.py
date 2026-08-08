class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in hmap:
                stack.append(c)
            else:
                if not stack or hmap[stack.pop()] != c:
                    return False
        return len(stack) == 0