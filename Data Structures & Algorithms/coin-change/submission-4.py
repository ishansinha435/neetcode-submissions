class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:   
        memo = {}

        def dfs(curr_sum):
            if curr_sum in memo:
                return memo[curr_sum]
            if curr_sum > amount:
                return float('inf')
            if curr_sum == amount:
                return 0
            res = 1 + min(dfs(curr_sum + n) for n in coins)
            memo[curr_sum] = res
            return res
        
        res = dfs(0)
        return res if res != float('inf') else -1