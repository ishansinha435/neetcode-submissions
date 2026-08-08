class Solution:
    def isValid(self, s: str) -> bool:
        stack, valid = [], {'{' : '}', '[' : ']', '(' : ')'}
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if not stack or c != valid[stack.pop()]:
                    return False
        return not stack