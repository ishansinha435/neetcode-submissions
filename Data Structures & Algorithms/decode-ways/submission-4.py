class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s) : 1}
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                memo[i] = 0
                continue
            res = memo[i + 1] 
            if i != len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += memo[i + 2]
            memo[i] = res
        
        return memo[0]