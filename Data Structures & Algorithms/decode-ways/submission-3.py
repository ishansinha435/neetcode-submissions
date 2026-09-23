class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def decode(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            res = decode(i + 1) + (decode(i + 2) if i < len(s) - 1 and int(s[i:i+2]) <= 26 else 0)
            memo[i] = res
            return res
        
        return decode(0)