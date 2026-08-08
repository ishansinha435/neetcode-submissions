class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'{':'}', '[':']', '(':')'}
        stack = []
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if not stack or valid[stack.pop()] != c:
                    return False
        return not stack