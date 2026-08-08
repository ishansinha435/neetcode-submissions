class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 1
        for i in range(len(s) - 1, -1, -1):
            temp = dp1
            if s[i] == "0":
                dp1 = 0
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
                dp1 += dp2
            dp2 = temp
        return dp1
            
