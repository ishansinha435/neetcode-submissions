class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0 : 0}
        for amt in range(1, amount + 1):
            prev_count = float('inf')
            for c in coins:
                if amt - c in dp:
                    prev_count = min(prev_count, dp[amt - c])
            if prev_count != float('inf'):
                dp[amt] = prev_count + 1
        return dp[amount] if amount in dp else -1

