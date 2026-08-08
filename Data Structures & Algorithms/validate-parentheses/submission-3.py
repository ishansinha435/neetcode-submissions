class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            if c in hashmap:
                if not stack or stack.pop(-1) != hashmap[c]:
                    return False
        if len(stack) != 0: return False
        return True
        