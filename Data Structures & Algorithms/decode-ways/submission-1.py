class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1 
            if s[i] == "0":
                return 0

            count = 0
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
                count = dfs(i + 1) + dfs(i + 2)
            else:
                count = dfs(i + 1)
            memo[i] = count
            return count
            
        return dfs(0)