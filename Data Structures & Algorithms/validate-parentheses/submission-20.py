class Solution:
    def isValid(self, s: str) -> bool:
        stack, valid = [], {'(':')','{':'}','[':']'}
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if not stack or valid[stack.pop()] != c:
                    return False
        return len(stack) == 0