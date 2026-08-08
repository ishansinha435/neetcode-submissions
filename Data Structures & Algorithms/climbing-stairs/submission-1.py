class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(steps):
            if steps == n:
                return 1
            if steps > n:
                return 0
            return dfs(steps + 1) + dfs(steps + 2)
        
        return dfs(0)