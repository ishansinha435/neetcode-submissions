class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        accept = {'(' : ')', '{' : '}', '[' : ']'}
        for char in s:
            if char in accept:
                stack.append(char)
            else:
                if not stack or accept[stack.pop()] != char:
                    return False
        
        if stack:
            return False
        return True