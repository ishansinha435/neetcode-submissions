class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 1
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                res = 0
            else:
                res = one
            if i != len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += two
            one, two = res, one
        
        return one