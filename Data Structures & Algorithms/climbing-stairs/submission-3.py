class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(steps):
            if steps >= n:
                return steps == n
            if steps in dp:
                return dp[steps]
            dp[steps] = dfs(steps + 1) + dfs(steps + 2)
            return dp[steps]
        
        return dfs(0)