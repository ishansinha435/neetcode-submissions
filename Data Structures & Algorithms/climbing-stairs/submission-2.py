class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(steps):
            if steps >= n:
                return steps == n
            one = dp[steps + 1] if steps + 1 in dp else dfs(steps + 1)
            two = dp[steps + 2] if steps + 2 in dp else dfs(steps + 2)
            dp[steps] = one + two
            return one + two
        
        return dfs(0)