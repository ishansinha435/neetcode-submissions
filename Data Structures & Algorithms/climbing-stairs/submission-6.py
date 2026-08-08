class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(steps):
            if steps in memo:
                return memo[steps]
            if steps > n:
                return 0
            if steps == n:
                return 1
            total = dfs(steps + 1) + dfs(steps + 2)
            memo[steps] = total 
            return total
        
        return dfs(0)